
wfjt = v2.workflow_job_templates.get(name="High Capacity Workflow")['results'][0]
wfj = wfjt.launch().wait_until_completed(timeout=1800, interval=30)
print("Workflow job is {}".format(wfj.id if wfj else None))

