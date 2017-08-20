from rpc.json.message.Request import Request


class HelloProxy(object):
     
    def __init__(self, client):
        super().__init__()
        self.client = client
   
    def giveName(self, name):
        return self.client.call('HelloService.giveName', {"name":name})
   
    def sayName(self):
        return self.client.call('HelloService.sayName', None)
     
    def add(self, a, b):
        return self.client.call('HelloService.add',  {'a':a, 'b':b})

    def giveName2(self, name):
        return self.client.call('Hello.giveName', {"name":name}) 

    def sayName2(self):
        return self.client.call("Hello.sayName", None)
    
    def add2(self, a, b):
        return self.client.call("Hello.add", {"a":a,"b":b})
        
    def attach(self, callback):
        return self.client.add_subscription('HelloService.attach', None, self.callback_decorator(callback))
       
    
     
    def detach(self, callback):
        return self.client.add_subscription('HelloService.detach', None, self.callback_decorator(callback))
        
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
    hello.giveName("sunshyran")
    print(hello.sayName())
    print(hello.add(1, 2))
    print("-----------another way but has the same result---------")
    hello.giveName2("sunshyran")
    print(hello.sayName2())
    print(hello.add2(1, 2))
    
    
    
    