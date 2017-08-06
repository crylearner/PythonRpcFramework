'''
Created on 2015年12月20日

@author: sunshyran
'''

import unittest

from rpc.framework.driver.Invoker import Invoker
from rpc.framework.driver.InvokerHandler import InvokerHandler
from test.rpcframework.FakeChannel import FakeChannel


class InovkerHandlerTest(unittest.TestCase):
    

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test(self):
        handler = InvokerHandler(FakeChannel())
        handler.startup()
        handler.invoke(Invoker(1, 'msg1'))
        handler.invoke(Invoker(2, 'msg2'))
        msg1 = handler.retrieve()
        msg2 = handler.retrieve()
        self.assertTrue(msg1=='msg1', msg1)
        self.assertTrue(msg2=='msg2', msg2)
        handler.shutdown()
        self.assertTrue(True) # 可以正常shutdown
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    