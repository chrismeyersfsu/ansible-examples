all:
	# HACK: The env variable is needed until https://github.com/ansible/ansible/pull/56194 lands 
	ANSIBLE_COLLECTIONS_PATHS=collections/  ansible-inventory -i my_inventory.yml --list --export
	ANSIBLE_CACHE_PLUGIN_CONNECTION=./fact_cache ANSIBLE_CACHE_PLUGIN=redhat.cmeyers.my_cache ANSIBLE_CALLBACK_WHITELIST=redhat.cmeyers.my_callback ansible-playbook -i my_inventory.yml main.yml
