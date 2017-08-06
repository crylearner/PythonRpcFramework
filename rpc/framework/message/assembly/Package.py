'''
Created on 2015-5-25

@author: 23683
'''
import struct

from rpc.framework.exception.AssemblyError import AssemblyError
from rpc.framework.log.RPCLog import RPCLog


class RpcPackage(object):
    '''
    package used to transmit on channel.
    \ 由于tcp长链接会出现粘包、半包的问题，因此加入专门的头、size、尾 方便定位。这个类提供了一个简单的实现
    \b 格式: RPC@[message size][message]#rpc
    '''

#    pack_format='@'
#                + 'BBBB' #'@RPC'
#                + 'L' #message size, NOT include head and tail
#                + 's' #rpc message
#                + 'BBBB' #'#rpc'
 
    pack_format= '4sL%ds4s'
    HAED    = b'RPC@'
    TAIL    = b'#rpc'

    
    def __init__(self):
        '''
        Constructor
        '''
        self.message        = bytes()  # rpc message that has been serialized
        
    
    def __str__(self):
        return str(bytes().join((self.HAED, self.message, self.TAIL)))
    
    
    @classmethod
    def minSize(cls):
        return struct.calcsize(cls.pack_format % 0)
    
    @classmethod
    def size(cls, message):
        return struct.calcsize(cls.pack_format % len(message))
    
    @classmethod
    def encode(cls, message):
        '''
        return bytes object of the pacakge
        '''
        messagelen = len(message)
        packformat=cls.pack_format % messagelen
        #print(packformat)
        return struct.pack(packformat, cls.HAED, messagelen, message, cls.TAIL)
        
    @classmethod
    def decode(cls, databytes):
        ''' 
        return rpc message from databytes
        when failed, if databytes is too short, then return None, otherwise raise Exception.
        '''
        if len(databytes) < cls.minSize():  return None
        (head, size) = struct.unpack('<4sL', databytes[0:8])
        if head != cls.HAED:
            RPCLog.getLogger().error(cls.__name__, "decode package failed for bad head:" + str(head))
            raise AssemblyError('Bad head(%s) occurs when RpcPackage::decode()' % str(head))
        
        if len(databytes) < size + cls.minSize(): return None
        format = '%ds4s' % size
        (message, tail) = struct.unpack(format, databytes[8:])
        if tail != cls.TAIL:
            RPCLog.getLogger().error(cls.__name__, "decode package failed for bad tail:" + tail)
            raise AssemblyError('Bad head(%s) occurs when RpcPackage::decode()' % str(head))
        
        return message
        
        
        
if __name__ == '__main__':
    print(RpcPackage.minSize())
    package = RpcPackage()
    package.message = b'abc'
    print(package)
    print(RpcPackage.encode(package.message))
    package2 = RpcPackage()
    package2.decode(b'RPC@\x06\x00\x00\x00abc#rpc')
    assert(package2.decode(b'RPC@\x07\x00\x00abc#rpc') == None)
    package2.decode(b'RPdC@\x07\x00\x00abc#rpc')
    
    
    
    