.PHONY: venv no_error error

venv:
	#virtualenv ./venv
	#. ./venv/bin/activate
	git clone https://github.com/ansible/ansible.git || true
	. ansible/hacking/env-setup

no_error:
	ansible localhost -i fake_inv_script.py -m ping

error: 
	ANSIBLE_DEBUG=True ANSIBLE_CACHE_PLUGINS=./ ANSIBLE_CACHE_PLUGIN=dummy_fact_cache ansible localhost -i fake_inv_script.py -vvvvv -m ping
