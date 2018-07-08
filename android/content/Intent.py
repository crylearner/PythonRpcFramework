'''
Created on 2018年7月7日

@author: sunshyran
'''
from android.content.ComponentName import ComponentName
from android.os.Bundle import Bundle
from robotide import action


class Intent(object):
    
    def __init__(self, action=None, component=None, category=None, data=None, type=None, extras=None, flags=0):
        self._component = component #ComponentName
        self._action    = action #string
        self._category  = category #list
        self._data      = data #uri
        self._type      = type #string
        self._extras    = extras #Bundle
        self._flags     = flags #int
        
        
    def toJson(self):
        result = {
                'action':self._action,
                'category':self._category,
                'data':self._data,
                'type':self._type,
                'flags':self._flags}
        if self._component:
            result['component'] = self._component.toJson()
        if self._extras:
            result['extras'] = self._extras.toJson()
        return result
            
    
    @classmethod    
    def fromJson(cls, jsondata):
        return Intent(action=jsondata.get('action'),
                      component=jsondata.get('component'),
                      category=jsondata.get('category'),
                      data=jsondata.get('data'),
                      type=jsondata.get('type'),
                      extras=Bundle(**jsondata.get('extras', {})),
                      flags=jsondata.get('flags'))
        
    def setAction(self,action):
        self._action = action
        return self
    
    def getAction(self):
        return self._action
    
    def getExtras(self):
        return self._extras
    
    def putExtras(self, extras):
        self._extras = extras
        return self
    
    def replaceExtras(self, extras):
        self._extras = extras
        return self
    
    def putExtra(self, name, value):
        if self._extras is None: self._extras = Bundle()
        self._extras.put(name, value)
        return self

    def hasExtra(self, name):
        if self._extras is None: return False
        return name in self._extras
        
    def getExtra(self, name, default=None):
        if self._extras is None:
            return None
        return self._extras.get(name, default)
    
    def setFlags(self, flag):
        self._flags = flag
        return self
        
    def addFlags(self, *flag):
        for f in flag:
            self._flags |= f
        return self

    def setPackage(self, package):
        self._package = package
        return self
    
    def getPackage(self):
        return self._package
    
    def setComponent(self, component):
        self._component = component
        return self
    
    def getComponent(self):
        return self._component
    
    def setClass(self, packageName, className):
        self.setComponent(ComponentName(packageName, className))
        return self
    
    
    def setData(self, data):
        self._data = data
        self._type = None
        return self
        
    def getData(self):
        return self._data
    
    def setType(self, type):
        self._type = type
        self._data = None
        return self
    
    def getType(self):
        return self._type
    
    def setDataAndType(self, data, type):
        self._type = type
        self._data = data
        return self
    
    def addCategory(self, *category):
        if self._category is None:
            self._category = []
        self._category.extend(category)
        return self
        
    def removeCategory(self, *category):
        if self._category is None: return self
        for c in category:
            self._category.remove(c)
        if len(self._category):
            self._category = None
        return self

if __name__ == '__main__':
    pass