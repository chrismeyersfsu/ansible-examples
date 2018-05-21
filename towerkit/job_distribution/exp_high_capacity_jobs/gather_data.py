import time
import json
import csv


jobs = v2.jobs.get(page_size=200, status='successful', launch_type='workflow')
jobs_json = []
for j in jobs.results:
    jobs_json.append(j.json)

with open('jobs.json', 'w') as outfile:
    json.dump(jobs_json, outfile)

with open('jobs.csv', 'w') as csvfile:
    fieldnames = ['id', 'started', 'finished', 'execution_node']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for job in jobs_json:
        writer.writerow(dict((k, job[k]) for k in fieldnames))

