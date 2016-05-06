#!/usr/bin/python

import time
import signal

def main():
    module = AnsibleModule(
        argument_spec = dict(
            seconds   = dict(type='int'),
        )
    )

    def sighandler():
        pass

    for i in [x for x in dir(signal) if x.startswith("SIG")]:
        try:
            signum = getattr(signal,i)
            signal.signal(signum,sighandler)
        except Exception:
            pass
            #print "Skipping %s"%i

    sleep_time_seconds = module.params.get('seconds', 1)
    time.sleep(sleep_time_seconds)
    module.exit_json(changed=True, sleep=sleep_time_seconds)

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()


