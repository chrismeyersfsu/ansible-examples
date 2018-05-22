100 hosts
1 inventory
1 Job Templates <allow_simultaneous=True, forks=19>
1 Workflow w/ 100 nodes parallel
chrismeyersfsu/ansible-examples/sleep.yml playbook sleeps between 5-20 seconds

jobs.json - ansible tower /api/v2/jobs/ workflows jobs that ran during the experiment as json data. This contains all of the data for each job detail endpoint.
jobs.csv - subset of jobs.json as csv. Fields: id, started, finished, execution_node 

The experiment sizes job needed capacity to match that of instance capacity. Ideally, each Instance would only run one job. Instead, we see the effect of celery pulling jobs off the queue as fast as possible and the result is Instance's that run more than they have capacity for, 2 jobs in paralell and not just 1.
