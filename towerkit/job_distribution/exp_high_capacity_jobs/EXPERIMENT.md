100 hosts
1 inventory
1 Job Templates <allow_simultaneous=True, forks=50>
1 Workflow w/ 100 nodes parallel
chrismeyersfsu/ansible-examples/sleep.yml playbook sleeps between 240-480 seconds

jobs.json - ansible tower /api/v2/jobs/ workflows jobs that ran during the experiment as json data. This contains all of the data for each job detail endpoint.
jobs.csv - subset of jobs.json as csv. Fields: id, started, finished, execution_node 
