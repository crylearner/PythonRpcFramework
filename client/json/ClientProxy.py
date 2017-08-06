'''
Created on 2017年8月5日

@author: sunshyran
'''
from rpc.json.client.Client import Client
from rpc.json.message.Request import Request


class ClientProxy(object):
    
    def __init__(self, host, port):
        super().__init__()
        self.session = Client(host, port)
        
    def call(self, method, params, timeout=None):
        if not self.session: raise RuntimeError('session is None when call ' + str(method))
        request = Request()
        request.method = method
        request.params = params
        request.ID = self.session.genReqID()
        return self.session.request(request, timeout)
    
    def async_call(self, method, params, listener):
        if not self.session: raise RuntimeError('session is None when call ' + str(method))
        request = Request()
        request.ID = self.session.genReqID()
        request.method = method
        request.params = params
        return self.session.asyncrequest(request, listener)

if __name__ == '__main__':
    pass