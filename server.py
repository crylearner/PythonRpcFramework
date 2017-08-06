'''
Created on 2015年8月3日

@author: sunshyran
'''
from concurrent.futures._base import Executor
import threading
import time

from jsonrpc.server.SocketRPCServer import RPCServerManager


Executor
class HelloService():
    
    def __init__(self):
        self.callback = []
        threading.Thread(target=self.__notify).start()
        
      
    def sayHello(self):
        return 'Hello World'
    
    def whoAreYou(self):
        return 'I am server'

    def add(self, a, b):
        return a + b
    
    def attach(self, callback):
        self.callback.append(callback)
    
    def detach(self, callback):
        print('detach', callback)
        self.callback.pop(self.callback.index(callback))
            
    def __notify(self):
        while True:
            for callback in self.callback: 
                callback('Hello, I\'m server')
            time.sleep(0.5)
            
            
if __name__ == '__main__':
    server = RPCServerManager()
    service = HelloService()
    server.registerService(service)
    server.start('127.0.0.1', 12345)