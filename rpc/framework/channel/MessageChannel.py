'''
Created on 2015年12月13日

@author: sunshyran
'''
from rpc.framework.channel.Channel import AbstractChannel
from rpc.framework.log.RPCLog import RPCLog
from rpc.framework.channel.ChannelError import ChannelDataError


class RpcMessageChannel(AbstractChannel):
    '''
    send and recv rpc message. so it has to know how to serialize rpc message to serialized object and how to reserialize
    And also, how to send and recv these serialized object
    '''
    def __init__(self, channel, serializer, deserializer, assembler):
        '''
        RpcMessageChannel channel装饰器.
        @param serializer 序列化rpc message
        @param deserializer  反序列化rpc message
        @param assembler  channel层次传输用的装配器
        '''
        super().__init__()
        self._internal_channel = channel
        self.assembler = assembler
        self.serializer = serializer
        self.deserializer = deserializer
        
        
    def send(self, message):
        '''
        @see Channel.AbstractChannel#send
        '''
        RPCLog.getLogger().debug(self.__class__.__name__, '\n'.join(('send ', str(message), '')))
        try:
            package = self.assembler.assemblePackage(self.serializer.serialize(message))
        except Exception as e:
            RPCLog.getLogger().exception(self.__class__.__name__, e)
            raise ChannelDataError(str(e))
        self._internal_channel.send(package)        
    
    
    def recv(self):
        '''
        see {@inheritDoc}
        '''
        try:
            message = self.deserializer.deserialize(self.assembler.assembleBytes(self._internal_channel.recv()))
        except Exception as e:
            RPCLog.getLogger().exception(self.__class__.__name__, str(e))
            raise ChannelDataError(str(e))
        RPCLog.getLogger().debug(self.__class__.__name__, '\n'.join(('recv ', str(message), '')))
        return message
    
    
    def close(self):
        '''
        @copydoc
        '''
        self._internal_channel.close()


