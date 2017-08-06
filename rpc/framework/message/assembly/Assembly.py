'''
Created on 2015-8-10

@author: 23683
'''

from rpc.framework.exception.AssemblyError import AssemblyError
from rpc.framework.log.RPCLog import RPCLog
from rpc.framework.message.assembly.Package import RpcPackage


class Assembly(object):
    '''
    \字节流的转配和组装器
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.data = bytearray()  # data need to assembly
    
    
    def assembleBytes(self, databytes):
        '''将字节串组装为rpc message
        <p>如果字节串不足，则返回None。如果字节串多余，则会在下次组装时，将本次多余的拼接在开头
        @param databytes 字节串
        \实际组装的时候，需要考虑一下几种情形
        1. 
        2. 
        '''
        self.data += databytes
        #print(self.data)
        try:
            message = RpcPackage.decode(self.data)
            if message:
                self.data = self.data[RpcPackage.size(message):]
            return message
        except AssemblyError as e:
            RPCLog.getLogger().exception(self.__class__.__name__, 'assembleBytes failed')
            RPCLog.getLogger().warning(self.__class__.__name__, 'assembleBytes(): discard data bytes')
            self.data.clear() 
            return None
    
    def assemblePackage(self, message):
        '''
        \ 将rpc message 组装为 字节串
        @param message rpc消息对象
        '''
        return RpcPackage.encode(message)
        

if __name__ == '__main__':
    data = b'RPC@\x03\x00\x00\x00abc#rpc'
    assembly = Assembly()
    result = assembly.assembleBytes(data[0:4])
    assert(result == None)
    result = assembly.assembleBytes(data[4:10])
    assert(result == None)
    result = assembly.assembleBytes(data[10:])
    print(result)
    
        