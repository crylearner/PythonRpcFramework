'''
Created on 2018年7月7日

@author: sunshyran
'''
class ContentValues(dict):
    '''
    classdocs
    '''
    def __missing__(self, key):
        return None
        
    def put(self, key, value):
        super()[key] = value
    
    def get(self, key, default=None):
        return super().get(key, default)
    
    def toJson(self):
        return self


if __name__ == '__main__':
    c = ContentValues(name='yyf')
    print(c['name'])
    print(c['nkey'])
    print(c)