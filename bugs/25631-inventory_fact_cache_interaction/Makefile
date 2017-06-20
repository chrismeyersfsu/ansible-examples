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

tower_error:
	export ANSIBLE_LIBRARY=/var/lib/awx/venv/tower/lib/python2.7/site-packages/awx/plugins/library; \
	export ANSIBLE_CACHE_PLUGINS=/var/lib/awx/venv/tower/lib/python2.7/site-packages/awx/plugins/fact_caching; \
	export ANSIBLE_CACHE_PLUGIN=tower; \
	export ANSIBLE_CACHE_PLUGIN_CONNECTION=tcp://127.0.0.1:6564; \
	export CALLBACK_CONNECTION='FAKE'; \
	export FACT_QUEUE='FAKE'; \
	ANSIBLE_DEBUG=True ansible localhost -i fake_inv_script.py -vvvvv -m ping
