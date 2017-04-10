This project is an example use case of the artifact feature that can be used with Workflows in Tower. The contrived example is what one might do in their integration flow. Specifically, run an integration test that produces some set of results that is to be consumed downstream by another job to, for example, notify users as to the success or failure of the integration run.

There are two playbooks in this example that can be combined in a workflow to exercise artifact passing. 

`invoke_set_stats.yml` is the first playbook in the Workflow. The contents of `integration_results.txt` is first uploaded to the web. `set_stats` is then invoked to artifact the url of the uploaded `integration_results.txt` into the Ansible variable `integration_results_url`.

`use_set_stats.yml` is the second playbook in the Workflow consumes the Ansible extra variable `integration_results_url`. It calls out to the web using the `uri` module to get the contents of the file uploaded by the previous Job Template Job. Then, it simply prints out the contents of the gotten file.
