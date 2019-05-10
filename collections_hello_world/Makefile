all:
	# HACK: The env variable is needed until https://github.com/ansible/ansible/pull/56194 lands 
	# inventory plugin + cache plugin
	ANSIBLE_CACHE_PLUGIN_CONNECTION=./fact_cache ANSIBLE_COLLECTIONS_PATHS=collections/  ansible-inventory -i my_inventory_cache.yml --list --export
	# inventory plugin
	ANSIBLE_COLLECTIONS_PATHS=collections/  ansible-inventory -i my_inventory.yml --list --export
	# Fact cache
	ANSIBLE_CACHE_PLUGIN_CONNECTION=./fact_cache ANSIBLE_CACHE_PLUGIN=redhat.cmeyers.my_cache ANSIBLE_CALLBACK_WHITELIST=redhat.cmeyers.my_callback ansible-playbook -i my_inventory.yml main.yml
