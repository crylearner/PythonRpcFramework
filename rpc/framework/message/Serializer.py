'''
Created on 2015-8-8

@author: 23683
'''

class AbstractSerializer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
        
    def serialize(self, message):
        '''
        serialize message
        @param message: object of RpcMessage
        @return object that serialized
        '''
        raise NotImplementedError
        
    