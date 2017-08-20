'''
Created on 2017年8月6日

@author: sunshyran
'''

class RpcSubscriber(object):
    '''
    classdocs
    '''
    

    def __init__(self, params):
        '''
        Constructor
        '''
        self.mapping = {}
    
    
    def addSubject(self, subject):
        self.mapping.update(subject.getDict())
    
    def cancelAllSubject(self):
        for k,v in self.mapping:
            v.detach(self)
    
    def execute(self, request):
        self.mapping.get(request.getMethod()).attach()