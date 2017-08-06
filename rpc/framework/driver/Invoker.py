'''
Created on 2015年7月12日

@author: sunshyran
@note: 这是我在其他地方写过的一个模型，直接拿来用
'''
import threading


class Invoker(object):
    '''
    @统一的命令请求，内部不区分request还是notification或者是response
    @支持是否需要回复，可以用于表示request 还是notification
    '''

    ##
    # @param message: rpc package object。 
    # @param listener: 
    # @param needResponse: 
    def __init__(self, id, message, resultlistener=None, needResponse=True):
        '''
        Constructor
        '''
        self.id = id
        self.message = message
        self.needResponse = needResponse
        self.resultlistener = resultlistener
        
        self.result = None
        self.hasresult = False
        self.resultlocker = None
        
    
    def __str__(self):
        return str('id=%s message=%s response=%s' %(str(self.id), str(self.message), str(self.needResponse)))    
        
    def isNeedResponse(self):
        return self.needResponse
    
    def fillResult(self, result):
        self.result = result
        self.hasresult = True
    
    ##
    #  等待直到真正的结果出来           
    def wait(self, timeout=None):
        if not self.resultlocker: self.resultlocker = threading.Condition()
        with self.resultlocker:
            while not self.hasresult:
                if not self.resultlocker.wait(timeout): 
                    raise Exception('timeout')
   
   
    ##
    #  通知结果出来
    #  如何有注册resultlistener， 那么也会同时调用resultlistener
    def notify(self):
        if self.resultlocker:
            with self.resultlocker:
                self.resultlocker.notify()
        if self.resultlistener:
            self.resultlistener.onResult(self)
            