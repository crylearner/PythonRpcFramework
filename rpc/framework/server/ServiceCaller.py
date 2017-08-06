'''
Created on 2015年7月14日

@author: sunshyran
'''

class ServiceCaller():
    
    
    def __init__(self):
        pass
    
    @classmethod
    def call(cls, caller, parameter):
        if not parameter or len(parameter) == 0:
            return caller()
        return caller(**parameter)

