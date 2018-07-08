import inspect
import time

from rpc.json.message.Request import Request


def rpc(method=None, *params):
    def func_wrapper(func):
        def _internal_func(*args, **kwargs):
            return func(*args, **kwargs)
        return _internal_func
    return func_wrapper

def rpc_call(client, service=None, *params):
    pass

class HelloProxy(object):
     
    def __init__(self, client):
        super().__init__()
        self.client = client
    
    def giveName(self, name):
        print('ask givename')
#         return self.client.call('HelloService.giveName', {"name":name})
        return rpc_call(self.client, self.giveName, name);
   
    def sayName(self):
        print('ask sayName')
        return self.client.call('HelloService.sayName', None)
     
    def add(self, a, b):
        print('ask add')
        return self.client.call('HelloService.add',  {'a':a, 'b':b})
    
    def growUp(self):
        print('ask growup')
        return self.client.call('HelloService.growUp', None)
    
    def listenGrowUp(self, callback):
        print('ask listengrowup')
        return self.client.add_subscription('HelloService.listenGrowUp', {'Type':'growup'}, self.callback_decorator(callback))
    
    def unlistenGrowUp(self, callback):
        return self.client.cancel_subscription('HelloService.unlistenGrowUp', {'Type':'growup'}, self.callback_decorator(callback), 1)

    def giveName2(self, name):
        return self.client.call('Hello.giveName', {"name":name}) 

    def sayName2(self):
        return self.client.call("Hello.sayName", None)
    
    def add2(self, a, b):
        return self.client.call("Hello.add", {"a":a,"b":b})

    def growUp2(self):
        print('ask growup')
        return self.client.call('Hello.growUp', None)
        
    def observeAge(self, callback):
        return self.client.add_subscription('Hello.observeAge', {'Type':'growup'}, self.callback_decorator(callback))
     
    def unobserveAge(self, callback):
        return self.client.add_subscription('HelloService.unobserveAge', {'Type':'growup'}, self.callback_decorator(callback))
        
    def callback_decorator(self, callback, callbacklist={}):
        '''
        
        '''
        def __callback(*args):
            callback(*args)
        if not callback in callbacklist: callbacklist[callback] = __callback
        return callbacklist[callback]
    
    
if __name__ == '__main__':
#     from client.json.ClientProxy import ClientProxy
#     client = ClientProxy('127.0.0.1', 12346)
#     hello = HelloProxy(client)
#     hello.giveName("sunshyran")
#     print(hello.sayName())
#     print(hello.add(1, 2))
#     def callback(*args):
#         print('callback', args)
#     print(hello.listenGrowUp(callback))
#     print(hello.growUp())
#     #print(hello.unlistenGrowUp(callback))
#     print("-----------another way but has the same result---------")
#     hello.giveName2("sunshyran")
#     print(hello.sayName2())
#     print(hello.add2(1, 2))
#     print(hello.observeAge(callback))
#     print(hello.growUp2())
#     time.sleep(5)
    h = HelloProxy(None)
    print(h.giveName)
    print(h.giveName.__name__)
    print(h.giveName.__self__.__class__.__name__)
    print(inspect.getargspec(h.giveName))
    print(inspect.getfullargspec(h.giveName))
    print(inspect.getargspec(rpc_call))
    
    
    