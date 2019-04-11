#!/usr/bin/env python

import json

from flask import Flask
from flask import request

app = Flask(__name__)
job_event_counts = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.data:
        payload = json.loads(request.data) or request.data

        if 'job' in payload and 'event' in payload:
            job_id = payload['job']
            job_event_counts.setdefault(job_id, 0)
            job_event_counts[job_id] += 1
            print("Job {} total events {}".format(job_id, job_event_counts[job_id]))

    return ''


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8087, debug=True)

