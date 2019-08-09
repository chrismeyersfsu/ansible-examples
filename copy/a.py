import django.db.backends.utils as bakutils
import traceback
import os


bakutils.CursorDebugWrapper_orig = bakutils.CursorWrapper

fh = open('/tmp/log/outme.log.%s' % os.getpid(), 'wa')


def print_stack_in_project():
    stack = traceback.extract_stack()
    exempt = ['lib/python', 'settings.py', 'logging/__init__.py', 'awx-manage']
    for path, lineno, func, line in stack:
        flag_continue = False
        for e in exempt:
            if e in path:
                flag_continue = True
                break
        if flag_continue:
            continue

        fh.write('File "%s", line %s, in %s, \t%s\n' % (path, lineno, func, line))

class CursorDebugWrapperLoud(bakutils.CursorDebugWrapper_orig):
    def execute(self, sql, params=None):
        try:
            return super(CursorDebugWrapperLoud, self).execute(sql, params)
        finally:
            print_stack_in_project()
            fh.write(sql)
            fh.write('\n\n')
            fh.flush()

    def executemany(self, sql, param_list):
        try:
            return super(CursorDebugWrapperLoud, self).executemany(sql, param_list)
        finally:
            print_stack_in_project()
            fh.write(sql)
            fh.write('\n\n')
            fh.flush()

#bakutils.CursorDebugWrapper = CursorDebugWrapperLoud
bakutils.CursorWrapper = CursorDebugWrapperLoud

