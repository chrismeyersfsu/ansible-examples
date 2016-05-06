#!/bin/bash
python -m cProfile -o outme /Users/meyers/ansible/ansible/bin/ansible-playbook -i inventory main.yml >> stdout
pyprof2calltree -i outme
qcachegrind outme.log
