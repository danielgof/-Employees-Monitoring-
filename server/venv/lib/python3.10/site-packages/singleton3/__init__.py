'''
Created on May 15, 2012

@author: lwoydziak
'''

class Singleton(type):
    def __init__(cls, name, bases, dictionary):
        super(Singleton, cls).__init__(name, bases, dictionary)
        cls._instance = None

    def __call__(self, *args, **kw):
        if self._instance is None:
            self._instance = super(Singleton, self).__call__(*args, **kw)

        return self._instance