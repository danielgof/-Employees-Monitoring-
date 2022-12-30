'''
Created on May 15, 2012

@author: lwoydziak
'''
from singleton3 import Singleton

class aSingleton(object, metaclass=Singleton):
    def __init__(self):
        pass

def test_OnlyOneInstanceIsReturned():
    assert aSingleton() == aSingleton()