'''
Created on 2015年7月13日

@author: sunshyran
'''
import inspect
from framework.server.AbstractServiceRegister import AbstractServiceRegister


class AutoServiceRegister(AbstractServiceRegister):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.services = {}
        
        
    def register(self, obj, servicename=None):
        if inspect.ismethod(obj):
            return self.register_method(obj)
        elif inspect.isfunction(obj):
            return self.register_function(obj)
        elif hasattr(obj, '__class__') and inspect.isclass(obj.__class__):
            return self.register_class(obj)   
        else: raise Exception('unsupported object')
        
    def register_method(self, obj):
        if not inspect.ismethod(obj): return False
        servicename = obj.__self__.__class__.__name__
        self.services.setdefault(servicename, {})[obj.__name__] = obj
        return True
    
    def register_function(self, obj, servicename='Anonymous'):
        if not inspect.isfunction(obj): return False
        self.services.setdefault(servicename, {})[obj.__name__] = obj
        return True
    
    def register_class(self, obj, predicate=None):
        if not (hasattr(obj, '__class__') and inspect.isclass(obj.__class__)): 
            return False
        servicename = obj.__class__.__name__
        for (name, attr) in inspect.getmembers(obj, predicate):
            # 系统方法或者私有方法，不添加
            if name.startswith('__') or name.startswith('_' + servicename + '__'): continue
            #print(name)
            if inspect.ismethod(attr): self.register_method(attr)
            elif inspect.isfunction(attr): self.register_function(attr, servicename)
        return True
        
    def get_service(self, servicename):
        index = servicename.find('.')
        if index == -1 : 
            service_name = 'Anonymous'
            method_name = servicename
        else:   
            service_name = servicename[0:index]
            method_name = servicename[index+1:]
        return self.services.get(service_name, {}).get(method_name)
    
    def list_services(self, servicename=None):
        if servicename:
            return str({servicename:self.services.get(servicename, {})})
        else:
            return str(self.services)
        
        
if __name__ == '__main__':
    class AServer(object):
        def __init__(self):
            pass
        
        def sayHello(self):
            return 'Hello World'
        
        def whoAreYou(self):
            return 'I am server'
        
        def __kaos(self):
            pass
        
        def _kaos(self):
            pass
        
    obj = AServer()
    
    service = AutoServiceRegister()
    print(service.register_class(obj))
    print(service.list_services())
    print(service.get_service('AServer.sayHello'))  
    