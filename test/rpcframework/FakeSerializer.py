'''
Created on 2015年12月22日

@author: sunshyran
'''
from rpc.framework.message.Serializer import AbstractSerializer


class FakeSerializer(AbstractSerializer):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        
    
    def serialize(self, message):
        return message.encode('utf-8')
    

    