'''
Created on 2016年1月17日

@author: sunshyran
'''

from utils.log.Logger import Logger
import logging
class RPCLog(object):
    '''
    classdocs
    '''
    instance = None

    @classmethod    
    def getLogger(cls):
        if not cls.instance:
            cls.instance = Logger('RPC', r'rpc.log')
            cls.instance.setLevel(logging.DEBUG, logging.ERROR)
        return cls.instance 

    
if __name__ == '__main__':
    rpclogger = RPCLog.getLogger()
    rpclogger.debug('TEST', 'testlog')
    rpclogger.info('TEST', 'testlog')
    rpclogger.warning('TEST', 'testlog')
    rpclogger.error('TEST', 'testlog')
    rpclogger.critical('TEST', 'testlog')