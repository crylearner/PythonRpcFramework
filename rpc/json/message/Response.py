'''
Created on 2015-5-25

@author: 23683
'''
import json

from rpc.json.message.RpcMessage import RpcMessage, MSG_KEY_ID, MSG_KEY_ERROR, \
    MSG_KEY_RESULT, MSG_KEY_PARAMS


class Response(RpcMessage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.ID = 0
        self.result = None
        self.error = None
        
        
    def __str__(self):
        return self.encode()
    
        
    def encode(self):
        if self.error:
            return json.dumps({MSG_KEY_ID:self.ID, MSG_KEY_ERROR:self.error})
        else:
            return json.dumps({MSG_KEY_ID:self.ID, MSG_KEY_RESULT:self.result})
        
    
    def decode(self, bytestring):
        message = json.loads(bytestring)
        self.decodeFromJson(message)
        

    def decodeFromJson(self, message):
        if MSG_KEY_ID not in message:
            raise Exception("%s has no id" % str(message))
        self.ID = message.get(MSG_KEY_ID)
        
        if MSG_KEY_ERROR not in message and MSG_KEY_RESULT not in message:
            raise Exception("%s has neither result nor error words" %str(message))
        self.error = message.get(MSG_KEY_ERROR, None)
        self.result = message.get(MSG_KEY_RESULT, None)
        
        

    
    
if __name__ == '__main__':
    response = Response()
    response.ID = 1
    response.result = True
    print(response)
    response2 = Response()
    response2.decode(response.encode())
    print(response2)