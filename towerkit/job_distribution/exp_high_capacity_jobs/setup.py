import time
import sys, os
sys.path.append(os.path.join(os.getcwd(), '..', '..'))
from utils import (
    get_or_create,
    delete_all,
    cancel_all
)

inventory_vars = """ansible_connection: local"""
sleep_interval_vars = """---
sleep_min: 5
sleep_max: 20
"""
#sleep_min: 240
#sleep_max: 480

def determine_capacity(v2):
    for i in v2.instances.get()['results']:
        if i.capacity > 0:
            return i.capacity
    return None

forks = determine_capacity(v2)
if forks is None:
    raise RuntimeException("Capactiy not determinable")
forks = forks - 1
print("Forks set to {}".format(forks))

cancel_all(v2.jobs)
cancel_all(v2.workflow_jobs)

delete_all(v2.jobs)
delete_all(v2.workflow_jobs)
delete_all(v2.workflow_job_templates)
delete_all(v2.inventory)
delete_all(v2.job_templates)

org = get_or_create(v2.organizations, name='cmurders murder inc.')
inv = get_or_create(org.related.inventories, name='cmurders murdertown', organization=org, variables=inventory_vars)

for i in xrange(0, forks+5):
    h = get_or_create(inv.related.hosts, name='high-capacity-host-{}'.format(i), inventory=inv)

proj = get_or_create(v2.projects, name='Murder Tools', organization=org, scm_url='https://github.com/chrismeyersfsu/ansible-examples.git', wait=True)

jt = get_or_create(v2.job_templates, name="High Capacity JT - {} forks".format(forks), organization=org, inventory=inv, project=proj, extra_vars=sleep_interval_vars, playbook='sleep.yml', allow_simultaneous=True, forks=forks)

wfjt = get_or_create(v2.workflow_job_templates, name="High Capacity Workflow", organization=org)

parallel_count = 100
current_node_count = wfjt.related.workflow_nodes.get()['count']
if current_node_count < parallel_count:
    for i in xrange(0, parallel_count):
        wfjt.related.workflow_nodes.post(dict(unified_job_template=jt.id))

wfj = None

#org.delete()
#jt.delete()
#proj.delete()
#wfjt.delete()

