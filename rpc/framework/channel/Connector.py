'''
Created on 2015年12月12日

@author: sunshyran
'''



class AbstractChannelConnector(object):
    '''
    connect to server
    '''   
       
    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        
        
    def connect(self):
        '''
        \用于发起并创建一个channel
        '''
        raise  NotImplementedError
    