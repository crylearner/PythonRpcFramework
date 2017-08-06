'''
Created on 2015年7月14日

@author: sunshyran
'''

class AbstractServiceRegister(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def register(self, service, servicename):
        raise NotImplementedError
    
    def register_function(self, service, servicename):
        raise NotImplementedError
    
    def list_service(self, servicename=None):
        raise NotImplementedError
    
    def get_service(self, servicename):
        raise NotImplementedError
    
    