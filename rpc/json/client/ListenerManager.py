'''
Created on 2015年8月4日

@author: sunshyran
'''
import threading


class ListenerManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.listeners = {}
        self.locker = threading.Lock()
        
    def register(self, listener, sid=None):
        with self.locker:
            identity = sid
            if sid is None: identity = id(listener)
            self.listeners[identity] = listener
            return identity
        
    def unregister(self, listener, sid=None):
        with self.locker:
            identity = sid
            if sid is None: identity = id(listener)
            self.listeners.pop(id(listener), None)
            return identity
            
    def get_listener(self, identity):
        with self.locker:
            return self.listeners.get(identity, None)
    
    def get_identity(self, listener):
        with self.locker:
            for (key, value) in self.listeners.items():
                if value == listener: return key
            return 0
            