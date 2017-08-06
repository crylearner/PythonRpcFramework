'''
Created on 2016年4月9日

@author: sunshyran
'''
from rpc.framework.exception.RpcError import RpcError, ErrorCode


class HandlerBusyError(RpcError):
    '''
    when invoker handler is busy and cannot invoke any message, then raise this exception
    '''
    def __init__(self):
        super().__init__()
    
    
    def code(self):
        return ErrorCode.CHANNEL_CLOSED_ERROR
    
class HandlerStopError(RpcError):
    '''
    when invoker handler is stopped, then raise this exception
    '''
    def __init__(self):
        super().__init__()

    
    def code(self):
        return ErrorCode.CHANNEL_CLOSED_ERROR    

if __name__ == '__main__':
    pass