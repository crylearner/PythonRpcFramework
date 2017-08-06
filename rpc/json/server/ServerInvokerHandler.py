'''
Created on 2015年12月13日

@author: sunshyran
'''
from rpc.framework.driver.InvokerHandler import InvokerHandler


class ServerInvokerHandler(InvokerHandler):
    '''
    '''
    
    def __init__(self, channel):
        super().__init__(channel)
        
        
    def invoke(self, invoker):
        return super().invoke(invoker)
    
    
    def retrieve(self):
        return super().retrieve()
    
    