from rpc.json.message.Request import Request


class HelloProxy(object):
     
    def __init__(self, client):
        super().__init__()
        self.client = client
   
   
    def sayHello(self):
        return self.client.call('HelloService.sayHello', None)
     
    def whoAreYou(self):
        return self.client.call('HelloService.whoAreYou', None)
     
    def add(self, a, b):
        return self.client.call('HelloService.add',  {'a':a, 'b':b})

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
        
        '''
        def __callback(*args):
            callback(*args)
        if not callback in callbacklist: callbacklist[callback] = __callback
        return callbacklist[callback]
    
    
if __name__ == '__main__':
    from client.json.ClientProxy import ClientProxy
    client = ClientProxy('127.0.0.1', 12345)
    hello = HelloProxy(client)
    print(hello.add(1, 2))
    
    
    