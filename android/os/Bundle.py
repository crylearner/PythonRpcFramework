'''
Created on 2018年7月7日

@author: sunshyran
'''

class Bundle(dict):
    '''
    classdocs
    '''
    def __missing__(self, key):
        return None
        
    def put(self, key, value):
        super()[key] = value
    
    def get(self, key, default=None):
        return super().get(key, default)
    
    def putAll(self, other):
        super().update(other)
    
    def toJson(self):
        return self
        
if __name__ == '__main__':
    b = Bundle(name='yyf')
    print(b['name'])
    print(b['nkey'])
    print(b.toJson())