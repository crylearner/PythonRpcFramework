'''
Created on 2015年12月17日

@author: sunshyran
'''



class AbstractDeserializer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
        
        
    def deserialize(self, serialized_object):
        '''
        @param serizlized_object   
        @return concrete rpc message,  e.g. Request, Response, Notification
        '''
        raise NotImplementedError
    