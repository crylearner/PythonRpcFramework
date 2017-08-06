'''
Created on 2015年12月13日

@author: sunshyran
'''
import threading

from rpc.framework.driver.InvokerHandler import InvokerHandler
from rpc.framework.exception.HandlerError import HandlerStopError
from rpc.json.message.Notification import Notification


class ClientInvokerHandler(InvokerHandler):
    '''
    '''
  
    def __init__(self, channel):
        super().__init__(channel)
        self.invokerwaitinglist = {}
    
    def startup(self):
        super().startup()
        self.thread = threading.Thread(target = self.retrieveResponse, daemon = True)
        self.thread.start()
        
    def shutdown(self):
        super().shutdown()
        self.thread.join()  
            
    def invoke(self, invoker):
        if invoker.isNeedResponse():
            self.invokerwaitinglist[invoker.id] = invoker
        super().invoke(invoker)
        return invoker
    
    
    def retrieve(self):
        message = super().retrieve()
        if message.ID in self.invokerwaitinglist:
            invoker = self.invokerwaitinglist.pop(message.ID)
            invoker.fillResult(message)
            invoker.notify()
        return message
    
    
    def retrieveResponse(self):
        while True:
            try:
                msg = self.retrieve()
            except HandlerStopError:
                break;
            #print(msg)
            if isinstance(msg, Notification):
                # 来自服务端的通知消息
                #print('receive notification', str(msg))
                listener = self.listener_manager.get_listener(msg.callback)
                if listener: listener(msg)
        
        
    