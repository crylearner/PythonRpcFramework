'''
Created on 2015-6-12

@author: 23683
'''

import threading

from rpc.framework.utils.Singleton import singleton


@singleton
class IDGenerator(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.id = 0
        self.locker = threading.Lock()
        
    
    def getID(self):
        with self.locker:
            self.id += 1
        return self.id
    
    def reset(self):
        with self.locker:
            self.id = 0
            
            
if __name__ == '__main__':
    gen = IDGenerator()
    print(gen.getID())
    print(gen.getID())            