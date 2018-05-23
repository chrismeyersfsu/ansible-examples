import sys, os
sys.path.append(os.path.join(os.getcwd(), '..', '..'))

import six
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

test_job_distribution_algo()
