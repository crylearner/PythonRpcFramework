'''
Created on 2015-5-25

@author: 23683
'''
import json

from rpc.json.message.RpcMessage import MSG_KEY_METHOD, MSG_KEY_PARAMS, \
    MSG_KEY_ID, RpcMessage, MSG_ENCODE


class Request(RpcMessage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.method=""
        self.params=None
        self.ID = 0
    

    def __str__(self):
        return self.encode()
    
        
    def encode(self):
        return json.dumps({MSG_KEY_ID:self.ID, MSG_KEY_METHOD:self.method, MSG_KEY_PARAMS:self.params})
        
    
    def decode(self, bytestring):
        message = json.loads(bytestring.decode(MSG_ENCODE))
        self.decodeFromJson(message) 
       
        
    def decodeFromJson(self, message):
        if MSG_KEY_ID not in message:
            raise Exception("%s has no id" %str(message))
        else:
            self.ID = message.get(MSG_KEY_ID)
        
        if MSG_KEY_METHOD not in message:
            raise Exception("%s has no method" %str(message))
        else:
            self.method = message.get(MSG_KEY_METHOD)
            
        self.params = message.get(MSG_KEY_PARAMS, None)    



if __name__ == '__main__':
    request = Request()
    request.ID = 1
    request.method = "test"
    request.params = {"arg1": '中国'}
    print(request)
    request2 = Request()
    request2.decode(b'{"method": "test", "params": {"arg1": "\u4e2d\u56fd"}, "id": 1}')
    print(request2)

        