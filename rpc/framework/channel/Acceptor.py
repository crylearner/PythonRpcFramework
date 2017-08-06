'''
Created on 2015年12月12日

@author: sunshyran
'''

    
    
class AbstractChannelAccepter(object):
    '''
    a channel accepter interface. 
    
    '''
     
    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        
        
    def accept(self):
        '''
        @brief 用于接收来自对端的channel创建请求，并返回channel
        '''
        raise  NotImplementedError
    
