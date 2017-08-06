'''
Created on 2015-8-8

@author: 23683
'''
import json

from rpc.framework.message.Serializer import AbstractSerializer
from rpc.json.message.Notification import Notification
from rpc.json.message.Request import Request
from rpc.json.message.Response import Response
from rpc.json.message.RpcMessage import MSG_KEY_ID, MSG_KEY_METHOD, \
    MSG_KEY_PARAMS, MSG_ENCODE, MSG_KEY_ERROR, MSG_KEY_RESULT


class Serializer(AbstractSerializer):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
        
    def serialize(self, message):
        '''
        serialize message
        @param message: object of RpcMessage
        '''
        if isinstance(message, Request):
            return self.serializeRequest(message)
        elif isinstance(message, Response):
            return self.serializeResponse(message)
        elif isinstance(message, Notification):
            return self.serializeNotification(message)
        else:
            raise Exception('unknown message %s' %str(message))
        
        
    @classmethod
    def serializeRequest(cls, request):
        return request.encode().encode(encoding=MSG_ENCODE)
    
    @classmethod
    def serializeResponse(cls, response):
        return response.encode().encode(encoding=MSG_ENCODE)
    
    @classmethod
    def serializeNotification(cls, notification):
        return notification.encode().encode(encoding=MSG_ENCODE)
    
    