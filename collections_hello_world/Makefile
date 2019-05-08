all:
	# HACK: The env variable is needed until https://github.com/ansible/ansible/pull/56194 lands 
	ANSIBLE_COLLECTIONS_PATHS=collections/  ansible-inventory -i my_inventory.yml --list --export
	ansible-playbook -i my_inventory.yml main.yml
