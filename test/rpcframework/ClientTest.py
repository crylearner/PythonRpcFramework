'''
Created on 2015年12月22日

@author: sunshyran
'''
import time
import unittest

from framework.client.Client import AbstractClient
from framework.driver.Invoker import Invoker
from framework.driver.InvokerHandler import InvokerHandler
from test.rpcframework.FakeChannel import FakeChannel


class FakeClient(AbstractClient):
    
    def __init__(self):
        invokerhandler = InvokerHandler(FakeChannel())
        super().__init__(invokerhandler)
    
    
    def onResponse(self, rsp):
        print(rsp)
        
    
class ClientTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        client = FakeClient()
        client.start()
        client.asyncrequest(Invoker(1, 'test message'))
        time.sleep(1)
        client.stop()
        
    
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()