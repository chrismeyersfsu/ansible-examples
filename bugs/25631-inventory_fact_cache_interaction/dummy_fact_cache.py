# (c) 2014, Brian Coca, Josh Drake, et al
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
'''
DOCUMENTATION:
    cache: memory
    short_description: RAM backed, non persistent
    description:
        - RAM backed cache that is not persistent.
    version_added: historical
    author: core team (@ansible-core)
'''


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.cache import BaseCacheModule


class CacheModule(BaseCacheModule):

    def __init__(self, *args, **kwargs):
        print("init called")
        self._cache = {}

    def get(self, key):
        print("Get called")
        return self._cache.get(key)

    def set(self, key, value):
        print("Set called for {} value {}".format(key, value))
        self._cache[key] = value

    def keys(self):
        return self._cache.keys()

    def contains(self, key):
        val = key in self._cache
        print("Contains called for key {} val {}".format(key, val))
        return val

    def delete(self, key):
        del self._cache[key]

    def flush(self):
        self._cache = {}

    def copy(self):
        return self._cache.copy()

    def __getstate__(self):
        return self.copy()

    def __setstate__(self, data):
        self._cache = data
