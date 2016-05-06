#!/usr/bin/python

import ujson
from dogpile.core import Dogpile


def main():
    module = AnsibleModule(
        argument_spec = dict(
        )
    )

    module.exit_json(changed=False)

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()


