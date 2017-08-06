'''
Created on 2015年7月12日

@author: sunshyran
'''
from rpc.framework.driver.MessageDriver import AbstractMessageDriver
from rpc.framework.driver.MessageThread import MessageFullError, StopError, \
    MessageEmptyError, MessageThread
from rpc.framework.channel.ChannelError import ChannelBrokenError, \
    ChannelClosedError, ChannelDataError
from rpc.framework.exception.HandlerError import HandlerBusyError, \
    HandlerStopError
from rpc.framework.log.RPCLog import RPCLog


class InvokerHandler(AbstractMessageDriver):
    '''
    \ 支持异步的RPC消息处理者。 一方面负责自动将消息从这端发送出去，另一方面负责自动从对端接收RPC消息
    \ 内部通过引入两个线程以及对应的消息队列，实现消息的发送和接收并行。
    '''
    
    DEFAULT_TIMEOUT = None
    def __init__(self, channel):
        super().__init__()
        self.channel = channel
        self.invoking_thread = MessageThread(target=self.__dealing_invoker, name='invoking')
        self.retrieving_thread = MessageThread(target=self.__receive_invoker, name='retrieving')
        
        self.isrunning = False;
        
    
    def startup(self):
        '''
        @see MessageDriver.AbstractMessageDriver#startup
        '''
        print("MessageHandler startup")
        self.isrunning = True
        self.invoking_thread.start()
        self.retrieving_thread.start()
        
        
    def shutdown(self):
        '''
        @see MessageDriver.AbstractMessageDriver#shutdown
        <p>内部在停止消息队列之前，会先停止channel</p>
        '''
        print("MessageHandler shutdown")
        # 必须先停止依赖的数据通道，然后才能停止发送和接收线程
        self.isrunning = False
        self.channel.close() 
        self.invoking_thread.stopAndWait()
        self.retrieving_thread.stopAndWait()
        
        
    def invoke(self, invoker):
        '''
        invoke a rpc message
        <p> 这里是异步模型，仅仅将invoker放入invoker处理队列, 因此不会阻塞</p>
        @return InvokeResult
        '''
        if not self.isrunning:
            RPCLog.getLogger().error(self.__class__.__name__,'handler is not running yet')
            raise HandlerStopError("try to invoke before handler run")
        try:
            self.invoking_thread.push(invoker, self.DEFAULT_TIMEOUT)
        except MessageFullError:
            RPCLog.getLogger().error(self.__class__.__name__,'timeout when inovke %s' %invoker) 
            raise HandlerBusyError('inovke timeout')
        except StopError: 
            RPCLog.getLogger().critical(self.__class__.__name__,'fatal error when inovke %s' %invoker)
            raise HandlerStopError('inovke failed') 
           
        
    def retrieve(self):
        '''
        \ 从retrieve队列中取出一个消息。 
        @note: 会一直阻塞，直到取到一个。如果超时，则返回None
        @return: return a message. If failed for some reason, exception will be raised
        '''
        if not self.isrunning:
            RPCLog.getLogger().error(self.__class__.__name__,'handler is not running yet')
            raise HandlerStopError("try to retrieve before handler run")
        try: 
            message = self.retrieving_thread.pop(self.DEFAULT_TIMEOUT)
            return  message
        except MessageEmptyError: 
            pass #忽略
        except StopError : 
            RPCLog.getLogger().critical(self.__class__.__name__,'fatal error when retrieve')
            raise HandlerStopError('retrieve failed')
            
    
    
    def __dealing_invoker(self):
        while self.isrunning:
            try:
                # 不考虑超时。超时意味着暂时没有请求任务
                invoker = self.invoking_thread.pop()
            except StopError:
                RPCLog.getLogger().exception(self.__class__.__name__,'stop invoking thread for exception')
                break
            try:
                self.channel.send(invoker.message)
            except (ChannelBrokenError, ChannelClosedError):
                RPCLog.getLogger().exception(self.__class__.__name__, 'stop invoking thread for exception')
                break
            except ChannelDataError:
                continue
            
            
    def __receive_invoker(self):
        while self.isrunning:
            try :
                message = self.channel.recv()
            except (ChannelBrokenError, ChannelClosedError):
                RPCLog.getLogger().exception(self.__class__.__name__, 'stop retrieving thread for exception')
                break
            except ChannelDataError:
                continue
            except Exception:
                RPCLog.getLogger().exception(self.__class__.__name__, 'an exception happened when retrieving')
                continue
            
            if message is None: continue
            try:
                #不考虑满的情况
                self.retrieving_thread.push(message)
            except MessageFullError as e:
                RPCLog.getLogger().exception(self.__class__.__name__,'__receive_invoker: message(%s) is discard for %s' %(message, e))  
            except StopError:
                RPCLog.getLogger().exception(self.__class__.__name__,'stop retrieving thread for exception')
                break
            
        self.retrieving_thread.push(None) #FIXME:: add an empty message to avoid recv blocking