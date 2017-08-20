'''
Created on 2017年8月6日

@author: sunshyran
'''
class Attacher():
    def __init__(self, name, func):
        self.name = name
        self.func = func
        
class Detacher():
    def __init__(self, name, func):
        self.name = name
        self.func = func

class Subject(object):
    '''
    classdocs
    '''


    def __init__(self, attacher, detacher):
        '''
        Constructor
        '''
        self.attacher = attacher
        self.detacher = detacher
    
    def getDict(self):
        return {self.attacher.name:self.attacher.func,
                self.detacher.name:self.detacher.func}
    
    def attach(self, observer):
        self.attacher.func(observer)
    
    def detach(self, observer):
        self.detacher.func(observer)
            
    def observer_wrapper(self, observer):
        return observer        