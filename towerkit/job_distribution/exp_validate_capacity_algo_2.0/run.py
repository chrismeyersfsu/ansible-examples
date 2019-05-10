import sys, os
sys.path.append(os.path.join(os.getcwd(), '..', '..'))

import six
import time
import json
import csv
from utils import (
    get_or_create,
    delete_all,
    cancel_all
)

inventory_vars = """ansible_connection: local"""
sleep_interval_vars = """---
sleep_min: 5
sleep_max: 10
"""
#sleep_min: 240
#sleep_max: 480

def find_largest_capacity(v2):
    greatest_capacity = None
    for i in v2.instances.get()['results']:
        if i.capacity == 0:
            raise RuntimeError(six.text_type("Capacity is 0 on node {}").format(i))
        if not greatest_capacity or i.capacity > greatest_capacity:
            greatest_capacity = i.capacity
    return greatest_capacity

def test_job_distribution_algo():
    instances = v2.instances.get(order_by='hostname')['results']
    jobs_count = len(instances)
    over_capacity_forks = find_largest_capacity(v2) + 1
    half_capacity_instance_index = int(len(instances)/2)
    instances[half_capacity_instance_index].capacity_adjustment = .5
    instances = v2.instances.get(order_by='hostname')['results']

    org = v2.organizations.create()
    proj = v2.projects.create(organization=org,
                              scm_url='https://github.com/chrismeyersfsu/ansible-examples.git',
                              wait=True)
    inv = v2.inventory.create(variables=inventory_vars, organization=org)

    map(lambda i: inv.related.hosts.create(inventory=inv), xrange(0, over_capacity_forks))
    jt = v2.job_templates.create(organization=org, inventory=inv, project=proj,
                                 extra_vars=sleep_interval_vars,
                                 playbook='sleep.yml',
                                 allow_simultaneous=True,
                                 forks=over_capacity_forks)
    jobs = [jt.launch() for i in xrange(0, jobs_count)]
    map(lambda j: j.wait_until_completed(), jobs)

    instances_set = set([instance['hostname'] for instance in instances])
    jobs_set = set([job['execution_node'] for job in jobs])

    assert instances_set == jobs_set

    for i in xrange(0, half_capacity_instance_index):
        assert instances[i]['hostname'] == jobs[i]['execution_node']

# Smallest idle node chosen last when a job is too big
    assert instances[half_capacity_instance_index]['hostname'] == jobs[-1]['execution_node']

    for i in xrange(half_capacity_instance_index+1, len(instances)):
        assert instances[i]['hostname'] == jobs[i-1]['execution_node']


def test_job_distribution_group_spill_over():
    instances = v2.instances.get(order_by='hostname')['results']
    jobs_count = len(instances)*2
    forks = (find_largest_capacity(v2) - 1) / 2
    instances = v2.instances.get(order_by='hostname')['results']

    for ig in v2.instance_groups.get(controller__isnull=True)['results']:
        if ig['name'] != 'tower':
            ig.delete()

    '''
    2 Jobs per-instance. Testing the overflow
    '''
    org = v2.organizations.create()
    proj = v2.projects.create(organization=org,
                              scm_url='https://github.com/chrismeyersfsu/ansible-examples.git',
                              wait=True)
    inv = v2.inventory.create(variables=inventory_vars, organization=org)

    '''
    Given 9 instances

    ig1.policy_instance_list = [ instance1, instance2 ]
    ig2.policy_instance_list = [ instance3 ]
    ig3.policy_instance_list = [ instance4, instance5 ]
    ig4.policy_instance_list = [ instance6 ]
    ig5.policy_instance_list = [ instance7, instance8 ]
    ig6.policy_instance_list = [ instance9 ]
    ...
    '''
    i = 0
    while i < len(instances):
        ig = v2.instance_groups.create(name="group-{}".format(i))

        if i%2 == 0:
            policy_instance_list = []
            if i < len(instances):
                policy_instance_list.append(instances[i]['hostname'])
            if (i+1) < len(instances):
                policy_instance_list.append(instances[i+1]['hostname'])
            if len(policy_instance_list) > 0:
                ig.policy_instance_list = policy_instance_list
            i = i + 2
        else:
            if i < len(instances):
                ig.policy_instance_list = [instances[i]['hostname']]
            i = i + 1

    time.sleep(5)
    instance_groups = v2.instance_groups.get(controller__isnull=True)['results']


    map(lambda i: inv.related.hosts.create(inventory=inv), xrange(0, forks+1))
    jt = v2.job_templates.create(organization=org, inventory=inv, project=proj,
                                 extra_vars=sleep_interval_vars,
                                 playbook='sleep.yml',
                                 allow_simultaneous=True,
                                 forks=forks)
    map(lambda ig: jt.add_instance_group(ig), instance_groups)
    jobs = [jt.launch() for i in xrange(0, jobs_count)]
    map(lambda j: j.wait_until_completed(), jobs)

    i = 0
    while i < len(instances):
        if i%2 == 0:
            if i < len(instances):
                assert jobs[i]['execution_node'] == instances[i]['hostname']
            if (i+1) < len(instances):
                assert jobs[i+1]['execution_node'] == instances[i]['hostname']
        else:
            if i < len(instances):
                assert jobs[i]['execution_node'] == instances[i]['hostname']
        i = i + 1

#test_job_distribution_job_too_large_idle()
test_job_distribution_group_spill_over()
