"""
Pyson database lib
Type : Key, value
File : {dbname}.Json
Developer : github.com/AlirezaWDX
Github : github.com/AlirezaWDX/Pyson
Do not remove the copyright sign
COPYRIGHT 2019 | ALL RIGHTS RESERVED BY ALIREZA SADEGHI

MODIFIED BY @Mandofskii, ADDED DICTS Feature
"""

import os, json

class Pyson:

    # ==========================================================================

    def __init__(self, name: str, autodump=False):
        """Create a new database or connect to a existing database | autodump: optional"""
        self.location = os.path.expanduser(str(name) + '.json')
        self.autodump = bool(autodump)
        self._load(self.location)
        return

    # ========================================================================== InApp functions

    def _load(self, location):
        if os.path.exists(location) == True:
            self.db = json.load(open(self.location, "rt"))
            self._autodump()
        else:
            self.db = {}
            self.db['_keys'] = {}
            self.db['_lists'] = {}
            self.db['_dicts'] = {}
            self._autodump()
        return True

    def _autodump(self):
        try:
            if self.autodump:
                json.dump(self.db, open(self.location, "w+"))
                return True
            else:
                return False
        except:
            return False

    # ========================================================================== Global functions

    def dump(self):
        """Force save from RAM to file"""
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False

    def reset(self):
        """Clear everything and reset database"""
        self.db = {}
        self.db['_keys'] = {}
        self.db['_lists'] = {}
        self.db['_dicts'] = {}
        self._autodump()
        return True

    def clearkeys(self):
        '''Reset all keys'''
        self.db['_keys'] = {}
        self._autodump()
        return True

    def cleardicts(self):
        '''Reset all dicts'''
        self.db['_dicts'] = {}
        self._autodump()
        return True

    def clearlists(self):
        '''Reset all lists'''
        self.db['_lists'] = {}
        self._autodump()
        return True

    # ========================================================================== Key, Value database

    def set(self, key, value):
        '''Set a value to a key'''
        try:
            self.db['_keys'][key] = value
            self._autodump()
            return True
        except Exception as e:
            print(e)
            return False

    def append(self, key, more):
        '''Append more to a key'''
        tmp = self.db[key]
        self.db[key] = tmp + more
        self._autodump()
        return True

    def rem(self, key):
        '''Delete a key'''
        try:
            del self.db['_keys'][key]
            self._autodump()
            return True
        except KeyError:
            print("Key not found.")
            return False

    def get(self, key):
        '''Get a value from a key'''
        try:
            return self.db['_keys'][key]
        except Exception as e:
            print(e)
            return False

    def getall(self):
        '''Get all keys and values'''
        return self.db['_keys']

    def keys(self):
        '''Get all keys'''
        return self.db['_keys'].keys()

    def values(self):
        '''Get all values'''
        return self.db['_keys'].values()

    def exists(self, key):
        '''Check if a key exists'''
        return key in self.db['_keys']

    def count(self):
        '''Get the lenth of keys | keys = values'''
        return len(self.db['_keys'].keys())

    # ========================================================================== List Key, Value database

    def createlist(self, name):
        self.db['_lists'][str(name)] = []
        self._autodump()
        return True

    def lset(self, name, value):
        try:
            if value not in self.db['_lists'][str(name)]:
                self.db['_lists'][str(name)].append(value)
                self._autodump()
            return True
        except Exception as e:
            print('lset exc')
            print(e)
            return False
    def lrem(self, name, value):
        try:
            if value in self.db['_lists'][str(name)]:
                for k,v in enumerate(self.db['_lists'][str(name)]):
                    index = k
                    if value == v:
                        break
                self.db['_lists'][str(name)].pop(index)
                self._autodump()
            return True
        except Exception as e:
            print(e)
            return False

    def lismember(self, name, value):
        return value in self.db['_lists'][name]

    def litems(self, name):
        return self.db['_lists'][name]


    def createdict(self, name):
        self.db['_dicts'][str(name)] = {}
        self._autodump()
        return True

    def dset(self, name, key, value):
        try:
            self.db['_dicts'][str(name)][key] = value
            self._autodump()
            return True
        except Exception as e:
            print('dset exc')
            print(e)
            return False
    def drem(self, name, key):
        try:
            if key in self.db['_dicts'][str(name)]:
                self.db['_dicts'][str(name)].pop(key)
                self._autodump()
            return True
        except Exception as e:
            print(e)
            return False

    def dget(self, name, key):
        if key in self.db['_dicts'][str(name)]:
            return self.db['_dicts'][str(name)][key]
        else:
            return False
