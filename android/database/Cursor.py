'''
Created on 2018年7月7日

@author: sunshyran
'''

class Cursor(object):
    
    def __init__(self, client, token):
        self._token = token
        self.client = client
    
    def fetch(self, size=1):
        '''
        @param size: -1 means all records
        '''
        rsp = self.client.call('Cursor.fetchmany', {'token':self._token, 'size':size})
        if rsp.error is not None:
            raise Exception(rsp.error)
        
        return rsp.result
    
    def fetchall(self):
        '''
        '''
        return self.fetch(-1)

    def fetchone(self):
        return self.fetch(1)    
    
    def getCount(self):
        rsp = self.client.call('Cursor.getCount', None)
        if rsp.error is not None:
            raise Exception(rsp.error)
        return rsp.result
        
    def close(self):
        self.client.call('Cursor.close', {'token':self._token})
    
    

if __name__ == '__main__':
    pass