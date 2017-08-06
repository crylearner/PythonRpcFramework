'''
Created on 2015年8月2日

@author: sunshyran
'''


import threading

class AbstractClient(object):
    
    def __init__(self, invoker_handler):
        self.handler = invoker_handler
        self.handler.startup()
    
        
    def stop(self):
        self.handler.shutdown()
    
    
    def request(self, invoker, timeout=5000):
        '''
        \ 同步阻塞调用，返回Response
        '''
        invoker = self.handler.invoke(invoker)
        invoker.wait(timeout)
        return invoker.result
    
    
    def asyncrequest(self, invoker):
        '''
        \ 异步非阻塞调用，返回None。结果处理由responseListener负责
        '''
        self.handler.invoke(invoker)
        return None
    
            
#     def listen(self, listener):
#         return self.listener_manager.register(listener)
#     
#     def cancelListener(self, listener):
#         return self.listener_manager.unregister(listener)
#             
#     def get_identity(self, listener):
#         return self.listener_manager.get_identity(listener)
#     
        