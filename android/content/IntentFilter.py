'''
Created on 2018年7月8日

@author: sunshyran
'''

class IntentFilter(object):
    
    
    def __init__(self, action=None, categories=None, data=None, type=None, priority=0):
        self._priority  = priority
        self._action    = action if action else set()
        self._categories= categories if categories else set()
        self._datatypes = type if type else set()
        self._uris      = data if data else set()
#         self._dataschemes=None
#         self._dataauthorities = None
#         self._datapaths = None
#         self.haspartialtypes  = False


    def toJson(self):
        return {'priority':self._priority,
                'action':self._action,
                'categories':self._categories,
                'datatypes':self._datatypes,
                'uri': self._uris}

    def getPriority(self):
        return self._priority

    def setPriority(self, priority):
        self._priority = priority
        return self

    def getActions(self):
        return self._action
    
    def addAction(self, *action):
        self._action.update(action)

    def getCategories(self):
        return self._categories

    def addCategories(self, *category):
        self._categories.update(category)
    
    def getDataTypes(self):
        return self._datatypes
    
    def addDataType(self, *datatype):
        self._datatypes.update(datatype)
        
    def getDataUri(self):
        return self._uris
    
    def addDataUri(self, *uri):
        '''
        1. 如果data的URI和datatype为空，则 filter 的URI和type也必须为空，才能匹配成功
        2. 如果data的URI不为空，但是datatype为空，则 filter 必须定义URI并匹配成功，且type为空，才能匹配成功
        3. 如果data的URI为空，但是datatype不为空，则 filter 必须URI为空，定义type并匹配成功，才能匹配成功
        4. 如果data的URI和data都不为空，则 filter 的URI和type都必须定义并匹配成功，才能匹配成功。
           <\r>对于URI部分，有一个特殊处理，就是即使filter没有定义URI，content和file两种URI也作为既存的URI存在
        '''
        
        self._uris.update(uri)
    
    
if __name__ == '__main__':
    intentf = IntentFilter()
    intentf.addAction("a", 'b')
    print(intentf.getActions())