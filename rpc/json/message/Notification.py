'''
Created on 2015-5-25

@author: 23683
'''

import json

from rpc.json.message.RpcMessage import MSG_KEY_ID, MSG_KEY_METHOD, \
    MSG_KEY_PARAMS, RpcMessage, MSG_KEY_CALLBACK


class Notification(RpcMessage):
    '''
    expand Json-Rpc 2.0: introduce new keyword 'callback' to notify who has subscribed this notification
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.method = ""
        self.params = None
        self.callback = 0 
    
    def __str__(self):
            return self.encode()
    
        
    def encode(self):
        if self.callback == 0:
            return json.dumps({MSG_KEY_METHOD:self.method, MSG_KEY_PARAMS:self.params})
        else:
            return json.dumps({MSG_KEY_METHOD:self.method, MSG_KEY_PARAMS:self.params, MSG_KEY_CALLBACK:self.callback})

    def decode(self, bytestring):
        message = json.loads(bytestring)
        self.decodeFromJson(message)


    def decodeFromJson(self, message):
        assert MSG_KEY_ID not in message
        if MSG_KEY_METHOD not in message:
            raise Exception("%s has no method" %str(message))
        else:
            self.method = message.get(MSG_KEY_METHOD)
        self.params = message.get(MSG_KEY_PARAMS, None)
        self.callback = message.get(MSG_KEY_CALLBACK, 0)
        

if __name__ == '__main__':
    notification = Notification()
    notification.method = "test"
    notification.params = {"arg1": 'x'}
    notification.callback = 1
    print(notification)
    notification2 = Notification()
    notification2.decode(notification.encode())
    print(notification2)      
      