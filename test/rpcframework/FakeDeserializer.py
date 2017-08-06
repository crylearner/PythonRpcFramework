'''
Created on 2015年12月22日

@author: sunshyran
'''
from framework.message.Deserializer import AbstractDeserializer


class FakeDeserializer(AbstractDeserializer):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        
    
    def deserialize(self, bytestring):
        return bytestring.decode('utf-8')
    
    