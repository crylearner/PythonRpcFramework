'''
Created on 2017年8月6日

@author: sunshyran
'''
from rpc.framework.log.RPCLog import RPCLog
from rpc.json.client.ListenerManager import ListenerManager

listenerManager = ListenerManager()
class RpcCallback(object):
    '''
    classdocs
    '''
    

    def __init__(self, callback):
        '''
        Constructor
        '''
        self._callback = callback
        global listenerManager
        self._callback_register = listenerManager
        
    
    def __call__(self, response):
        if response is None or response.result is None or "SID" not in response.result:
            RPCLog.getLogger().error(self.__class__.__name__, "response is invalid: %s" %str(response))
            return
        sid = response.result.get("SID")
        self._register_callback(self._callback, sid)
    
    
    def _register_callback(self, callback, sid):
        self._callback_register.register(callback, sid)
    
    def _unregister_callback(self, callback, sid):
        self._callback_register.unregister(callback, sid)
        