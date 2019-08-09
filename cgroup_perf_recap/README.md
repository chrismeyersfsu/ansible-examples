Play around with Ansible performance logging feature.
```
sudo cgcreate -a ec2-user:ec2-user -t ec2-user:ec2-user -g cpuacct,memory,pids:ansible_profile
cgexec -g cpuacct,memory,pids:ansible_profile ansible-playbook
```
