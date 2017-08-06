'''
Created on 2015年8月2日

@author: sunshyran
'''



from rpc.framework.channel.MessageChannel import RpcMessageChannel
from rpc.framework.channel.socket.SocketChannel import SocketChannelConnector
from rpc.framework.driver.Invoker import Invoker
from rpc.framework.exception.HandlerError import HandlerBusyError, \
    HandlerStopError
from rpc.framework.message.assembly.Assembly import Assembly
from rpc.framework.utils.IDGenerator import IDGenerator
from rpc.json.client.ClientInvokerHandler import ClientInvokerHandler
from rpc.json.message.Deserializer import Deserializer
from rpc.json.message.Serializer import Serializer
from rpc.framework.exception.RpcError import RpcTimeoutError


class Client(object):
    
    def __init__(self, host, port):
        self.reqidgen = IDGenerator()
        conn = SocketChannelConnector(host, port).connect()
        self.handler = ClientInvokerHandler(RpcMessageChannel(conn, Serializer(), Deserializer(), Assembly()))
        self.handler.startup()
        super().__init__()
        
    def request(self, req, timeout=5000):
        '''
        \ 同步阻塞调用，返回Response
        '''
        invoker = Invoker(req.ID, req)
        try:
            self.handler.invoke(invoker)
        except HandlerBusyError:
            raise RpcTimeoutError(req)
            return None #TODO: should raise exception
        except HandlerStopError:
            return None
        invoker.wait(timeout)
        return invoker.result
    
    
    def asyncrequest(self, req, responseListener):
        '''
        \ 异步非阻塞调用，返回None。结果处理由responseListener负责
        '''
        return super().asyncrequest(Invoker(req.ID, req, responseListener, False))
    
         
            
#     def listen(self, listener):
#         return self.listener_manager.register(listener)
#     
#     def cancelListener(self, listener):
#         return self.listener_manager.unregister(listener)
#             
#     def get_identity(self, listener):
#         return self.listener_manager.get_identity(listener)
#     


    def genReqID(self):
        return self.reqidgen.getID()
        