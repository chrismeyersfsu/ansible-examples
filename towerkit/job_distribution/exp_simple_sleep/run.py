
wfjt = v2.workflow_job_templates.get(name="Mass Murder")['results'][0]
wfj = wfjt.launch().wait_until_completed(timeout=600)
print("Workflow job is {}".format(wfj.id if wfj else None))

