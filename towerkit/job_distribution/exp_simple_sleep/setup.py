import time
import sys, os
sys.path.append(os.path.join(os.getcwd(), '..'))
from utils import get_or_create

host_vars = """ansible_connection: local"""
sleep_interval_vars = """---
sleep_min: 240
sleep_max: 480
"""

while True:
    jobs_req = v2.jobs.get(page_size=200)
    if jobs_req['count'] == 0:
        break
    for j in jobs_req['results']:
        j.delete()

org = get_or_create(v2.organizations, name='cmurders murder inc.')
inv = get_or_create(org.related.inventories, name='cmurders murdertown', organization=org)
h = get_or_create(inv.related.hosts, name='cmurder', variables=host_vars, inventory=inv)

proj = get_or_create(v2.projects, name='Murder Tools', organization=org, scm_url='https://github.com/chrismeyersfsu/ansible-examples.git', wait=True)

jt = get_or_create(v2.job_templates, name="Kill Number 1", organization=org, inventory=inv, project=proj, extra_vars=sleep_interval_vars, playbook='sleep.yml', allow_simultaneous=True)

wfjt = get_or_create(v2.workflow_job_templates, name="Mass Murder", organization=org)

parallel_count = 100
current_node_count = wfjt.related.workflow_nodes.get()['count']
if current_node_count < parallel_count:
    for i in xrange(0, parallel_count):
        wfjt.related.workflow_nodes.post(dict(unified_job_template=jt.id))

wfj = None
#wfj = wfjt.launch().wait_until_completed()
#print("Workflow job is {}".format(wfj.id if wfj else None))

#org.delete()
#jt.delete()
#proj.delete()
#wfjt.delete()

