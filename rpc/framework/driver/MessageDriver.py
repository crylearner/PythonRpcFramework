'''
Created on 2015年12月13日

@author: sunshyran
'''


class AbstractMessageDriver(object):
    '''
    a message driver.
    '''
    def __init__(self):
        super().__init__()
        
        
    def startup(self, channel):
        '''
        \ start driver
        '''
        raise NotImplementedError
    
    
    def shutdown(self):
        '''
        \ stop driver
        '''
        raise NotImplementedError
        
        
    def invoke(self, message):
        '''
        \ send rpc message
        '''
        raise NotImplementedError
    
    
    def retrieve(self):
        '''
        \ recv rpc message
        '''
        raise NotImplementedError

