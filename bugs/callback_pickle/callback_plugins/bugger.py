# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from datetime import datetime

from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.default import CallbackModule as DefaultCallbackModule

import cPickle as pickle
from io import BytesIO

import time


class CallbackModule(DefaultCallbackModule):
    """
    This callback module tells you how long your plays ran for.
    """
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'bugger'
    #CALLBACK_NEEDS_WHITELIST = True

    def __init__(self):

        super(CallbackModule, self).__init__()

    def v2_runner_on_ok(self, result):
        super(CallbackModule, self).v2_runner_on_ok(result)
        file = BytesIO()
        pickler = pickle.Pickler(file, protocol=0)
        pickler.dump(result._result)
        val = file.getvalue()

        '''
        f2 = BytesIO(val)
        unpickler = pickle.Unpickler(f2)
        res = unpickler.load()
        print(res)
        '''
