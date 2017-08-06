'''
Created on 2015年7月12日

@author: sunshyran
'''

class ServiceRegister(object):
    '''
    @服务注册  不考虑线程安全，这里简化起见，也不引入反射机制。
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.services = {}
        
    ## 注册具体的服务
    #  @param servicename: 服务名
    #  @param obj: 具体的对象
    def register(self, obj, servicename):
        if servicename in self.services:
            print('warning: %s is already registered' % servicename)
        else:
            self.services[servicename] = obj
    
    def get_service(self, servicename):
        return self.services[servicename]
    
    def list_service(self, servicename=None):
        if servicename:
            return str({servicename, self.services[servicename]})
        else:
            return str(self.services)


if __name__ == '__main__':
    services = ServiceRegister()
    services.register('sayHello', 1)
    services.register('whoAreYou', 2)
    print(services.list_service())
    print(services.get_service('sayHello'))

            