'''
Created on 2015年7月12日

@author: sunshyran
'''
import threading
import time

from rpc.json.client.Client import Client
from rpc.json.message.Request import Request


class HelloProxy(object):
     
    def __init__(self):
        super().__init__()
   
   
    def bindClient(self, client):
        self.client = client
   
    def sayHello(self):
        req = Request()
        req.ID = 1
        req.method = 'HelloService.sayHello'
        return self.client.request(req)
     
    def whoAreYou(self):
        req = Request()
        req.ID = 2
        req.method = 'HelloService.whoAreYou'
        return self.client.request(req)
     
    def add(self, a, b):
        req = Request()
        req.ID = 3
        req.method = 'HelloService.add'
        req.params = {'a':a, 'b':b}
        return self.client.request(req)

#     def attach(self, callback):
#         req = Request()
#         req.ID = 4
#         req.method = 'HelloService.attach'
#         cid = self.client.listen(self.callback_decorator(callback))
#         req.params = {'callback':cid}
#         return self.client.request(req)
#     
#     def detach(self, callback):
#         req = Request()
#         req.ID = 5
#         req.method = 'HelloService.detach'
#         cid = self.client.get_identity(self.callback_decorator(callback))
#         req.params = {'callback':cid}
#         
#         self.client.request(req)
#         self.client.cancelListener(self.callback_decorator(callback))
        
    def callback_decorator(self, callback, callbacklist={}):
        '''
        \ 可根据需要，对完整的参数列表做过滤
        '''
        def __callback(*args):
            callback(*args)
        if not callback in callbacklist: callbacklist[callback] = __callback
        return callbacklist[callback]

if __name__ == '__main__':

    client = Client('127.0.0.1', 12345)
    client.start()
    thread = threading.Thread(target = client.run, daemon = True).start()
    proxy = HelloProxy()
    proxy.bindClient(client)
    
    def callback(x):
        print(x)
    
    print(proxy.sayHello())
    print('cccc')   
    print(proxy.whoAreYou())
    print(proxy.add(1, 2))
#     print(proxy.attach(callback))
#     time.sleep(1)
#     print(proxy.detach(callback))
#     time.sleep(1)
    print('dddd')
    
    client.stop()
    
    