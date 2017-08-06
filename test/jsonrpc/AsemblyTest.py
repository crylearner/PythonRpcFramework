'''
Created on 2017年8月5日

@author: sunshyran
'''
import unittest

from rpc.framework.message.assembly.Assembly import Assembly
from rpc.json.message.Request import Request
from rpc.json.message.Serializer import Serializer
from rpc.json.message.Deserializer import Deserializer


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        req = Request()
        req.ID = 1
        req.method = 'call'
        req.params = {'a':2}
        asm = Assembly()
        bytes = asm.assemblePackage(Serializer().serialize(req))
        print(bytes)
        req2 = Deserializer().deserialize(asm.assembleBytes(bytes))
        self.assertEqual(str(req), str(req2))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()