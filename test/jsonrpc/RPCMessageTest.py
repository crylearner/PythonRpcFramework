'''
Created on 2015年12月23日

@author: sunshyran
'''
import unittest

from rpc.json.message.Deserializer import Deserializer
from rpc.json.message.Notification import Notification
from rpc.json.message.Request import Request
from rpc.json.message.Response import Response
from rpc.json.message.Serializer import Serializer


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testRequest(self):
        req = Request()
        req.ID = 1
        req.method = 'call'
        req.params = {'a':2}
        bytestring = Serializer().serialize(req)
        print(bytestring)
        req2 = Deserializer().deserialize(bytestring)
        self.assertTrue(req.ID == req2.ID)
        self.assertTrue(req.method == req2.method)
        self.assertDictEqual(req.params, req2.params)
        
    
    def testResponse(self):
        rsp = Response()
        rsp.ID = 1
        rsp.result = True
        bytestring = Serializer().serialize(rsp)
        print(bytestring)
        rsp2 = Deserializer().deserialize(bytestring)
        self.assertTrue(rsp.ID == rsp2.ID)
        self.assertTrue(rsp.result == rsp2.result)
        
    
    def testNotification(self):
        noti = Notification()
        noti.method = 'callback';
        noti.params = {'a':2}
        bytestring = Serializer().serialize(noti)
        print(bytestring)
        noti2 = Deserializer().deserialize(bytestring)
        self.assertTrue(noti.params == noti2.params)
        self.assertTrue(noti.method == noti2.method)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRequest']
    unittest.main()