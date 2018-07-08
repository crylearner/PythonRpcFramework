'''
Created on 2018年7月7日

@author: sunshyran
'''

class ComponentName(object):
    
    def __init__(self, className=None, packageName=None):
        self._class = className
        self._package = packageName
        
    def getPackageName(self):
        return self._package
    
    def getClassName(self):
        return self._class
    
    def toJson(self):
        return {"class":self._class, 'package':self._package}
    

if __name__ == '__main__':
    print(ComponentName('c', 'p').toJson())