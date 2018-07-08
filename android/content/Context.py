'''
Created on 2018年7月8日

@author: sunshyran
'''

class Context(object):
    
    def __init__(self, client):
        self.client = client
    
    def registerReceiver(self, receiver, filter, permission):
        pass
    
    def unregisterReceiver(self, receiver):
        pass

    def startService(self,intent):
        rsp = self.clent.call('Context.startService', {'intent':intent.toJson()})
        
        
    def stopService(self, intent):
        rsp = self.client.call('Context.stopService', {'intent':intent.toJson()})
        
    def startActivity(self, intent):
        rsp = self.client.call('Context.stopActivity', {'intent':intent.toJson()})
    
    def sendBroadcast(self, intent, permission):
        rsp = self.client.call('Context.sendBroadcast', {'intent':intent.toJson(), 'permission':permission})
    
    def sendOrderedBroadcast(self, intent, permission):
        rsp = self.client.call('Context.sendOrderedBroadcast', {'intent':intent.toJson(), 'permission':permission})
    
    def sendStickyBroadcast(self, intent):
        rsp = self.client.call('Context.sendStickyBroadcast', {'intent':intent.toJson()})

    def removeStickyBroadcast(self, intent):
        rsp = self.client.call('Context.sendStickyBroadcast', {'intent':intent.toJson()})


if __name__ == '__main__':
    pass