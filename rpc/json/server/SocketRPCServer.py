'''
Created on 2015年8月3日

@author: sunshyran
'''
import threading
import time
import traceback

from rpc.framework.channel.MessageChannel import RpcMessageChannel
from rpc.framework.channel.socket.SocketChannel import SocketChannelAcceptor
from rpc.framework.message.assembly.Assembly import Assembly
from rpc.framework.server.AutoServiceRegister import AutoServiceRegister
from rpc.framework.server.ServiceCaller import ServiceCaller
from rpc.json.message.Deserializer import Deserializer
from rpc.json.message.Serializer import Serializer
from rpc.json.server.Server import Server
from rpc.json.server.ServerInvokerHandler import ServerInvokerHandler


class RPCServerManager(object):
    '''
    RPCServerManager RPC服务管理类，负责启动或者停止RPC服务，以及注册RPC服务
    '''
    class ServerThread(threading.Thread):
        
        def __init__(self):
            super().__init__()
        
        def bindServer(self, server):
            self.server = server
        
        def stop(self):
            if not self.server : return
            self.server.terminate()
            
        def run(self):
            try:
                self.server.serve()
            except Exception as e :
                print(e)
                traceback.print_stack() 
                self.server.terminate() # FIXME:: 异常处理？
            self.server = None # 保证垃圾回收
    
    
    def __init__(self, service_register=None):
        '''
        @param service_register: 服务注册类。如果为None，则模式使用AutoServiceRegister
        '''
        if service_register: self.service_register = service_register
        else:self.service_register = AutoServiceRegister()
        
        self.isrunning = False
        self.MaxServerCount = 10
        self.workingthread = []
        for i in range(self.MaxServerCount):
            self.workingthread.append(RPCServerManager.ServerThread())
        
    
    def start(self, host,  port):
        self.channel_acceptor = SocketChannelAcceptor(host, port)
        self.isrunning = True
        while self.isrunning:
            conn =  self.channel_acceptor.accept()
            handler = ServerInvokerHandler(RpcMessageChannel(conn, Serializer(), Deserializer(), Assembly()))
            server = Server(handler, self.caller)
            thread = self.getStandbyWorkingThread();
            thread.bindServer(server);
            thread.start()

    def stop(self):
        '''
        \ 目前还不支持停止server. 尚未找到好的模型
        '''
        for thread in self.workdingthread: thread.stop()
        self.channel_acceptor.interrupt()
        self.isrunning = False
    
    
    def registerService(self, service):
        self.service_register.register(service)
        #print(self.service_register.list_services())
        return self


    def caller(self, command, parameter):
        fun = self.service_register.get_service(command)
        if not fun: raise Exception('service \"%s\" is not found' %command)
        return ServiceCaller.call(fun, parameter)
    
    
    def getStandbyWorkingThread(self):
        while self.isrunning:
            for thread in self.workingthread:
                if not thread.is_alive(): return thread
            time.sleep(0.1)

    
if __name__ == '__main__':
    pass