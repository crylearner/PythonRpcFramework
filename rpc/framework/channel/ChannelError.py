'''
Created on 2015年12月12日

@author: sunshyran
'''
from rpc.framework.exception.RpcError import RpcError, ErrorCode


class ChannelBrokenError(Exception):
    '''
    when send or recv on a broken channel, this exception will be raised
    @note broken means channel can not do transmission, but not been closed yet.
    '''
    pass

class ChannelClosedError(RpcError):
    '''
    when send or recv on a closed channel, this exception will be raised
    '''
    def __init__(self):
        super().__init__()
    
    
    def code(self):
        return ErrorCode.CHANNEL_CLOSED_ERROR
    
         
class ChannelDataError(Exception):
    '''when send or recv unsupported data, this exception will be raised
    '''
    pass


if __name__ == '__main__':
    error = ChannelClosedError()
    print(error)