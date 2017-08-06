'''
Created on 2015-6-15

@author: 23683
'''

#class Singleton(object):
#    '''
#    classdocs
#    '''
#
#
#    def __init__(self):
#        '''
#        Constructor
#        '''

def singleton(cls):
    instance = {}
    def __singleton(*args, **kw):
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return __singleton