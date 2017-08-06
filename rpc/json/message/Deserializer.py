'''
Created on 2015年12月17日

@author: sunshyran
'''

import json

from rpc.framework.message.Deserializer import AbstractDeserializer
from rpc.json.message.Notification import Notification
from rpc.json.message.Request import Request
from rpc.json.message.Response import Response
from rpc.json.message.RpcMessage import MSG_ENCODE, MSG_KEY_METHOD, MSG_KEY_ID, \
    MSG_KEY_RESULT


class Deserializer(AbstractDeserializer):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
        
        
    def deserialize(self, bytestring):
        '''
        return concrete rpc message,  e.g. Request, Response, Notification
        '''
        message = json.loads(bytestring.decode(MSG_ENCODE))
        if MSG_KEY_METHOD in message and MSG_KEY_ID in message:
            return self.deserializeRequest(message)
        
        elif MSG_KEY_METHOD in message and MSG_KEY_ID not in message:
            return self.deserializeNotification(message)
            
        elif MSG_KEY_RESULT in message:
            return self.deserializeResponse(message)
        
        else:
            raise Exception('unsupported package %s' %str(message))
    
    
    @classmethod
    def deserializeRequest(cls, message):
        request = Request()
        request.decodeFromJson(message)
        return request
    
    
    @classmethod
    def deserializeResponse(cls, message):
        response = Response()
        response.decodeFromJson(message)
        return response
   
   
    @classmethod
    def deserializeNotification(cls, message):
        notification = Notification()
        notification.decodeFromJson(message)
        return notification
        
        
   


if __name__ == '__main__':
    pass