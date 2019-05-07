#!/usr/bin/env python

from ansible_collections.redhat.cmeyers.plugins.module_utils.my_shared_lib import return_hello_world
import json
from ansible.module_utils.basic import AnsibleModule

def main():
    results = dict(
        changed=False,
        source=return_hello_world()
    )
    AnsibleModule(argument_spec=dict()).exit_json(**results)


if __name__ == '__main__':
    main()

