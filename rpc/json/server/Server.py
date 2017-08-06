'''
Created on 2015年8月1日

@author: sunshyran
'''

from rpc.framework.driver.Invoker import Invoker
from rpc.json.message.Request import Request
from rpc.json.message.Response import Response


class Server():
    
    def __init__(self, handler, caller):
        '''
        @param caller: caller(command, param)
        '''
        self.handler = handler
        self.caller = caller
        

    def serve(self):
        '''
        start rpc service
        @note: 不可重入
        '''
        self.isrunning = True
        self.handler.startup()
        while self.isrunning:
            message = self.handler.retrieve()
            self.__dealingWithRequest(message)
            
            
    def terminate(self):
        self.isrunning = False
        self.handler.shutdown()
              
    
    def __dealingWithRequest(self, req):
        '''
        '''
        rsp = Response()
        rsp.ID = req.ID
        print('req', req)
        # 需要处理订阅 还是普通的请求
#         if req.params and 'callback' in req.params:
#             req.parameter['callback'] = self.callback_decorator(req.parameter['callback'])
        try:
            rsp.result = self.caller(req.method, req.params)
        except Exception as e:
            print(e)
            rsp.error = str(e)
                
        #print('result', rsp)
        self.handler.invoke(Invoker(rsp.ID, rsp, None, False))
        
        
        

        
