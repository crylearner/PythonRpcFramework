'''
Created on 2015年12月20日

@author: sunshyran
'''
import time
import unittest

from rpc.framework.driver.MessageThread import MessageThread, MessageEmptyError, \
    MessageFullError, StopError


class MessageThreadTest(unittest.TestCase):


    def setUp(self):
        self.messagethread = MessageThread('', self._run)
        self.messagethread.start()

    def tearDown(self):
        self.messagethread.stop()  

    def _run(self):
        while self.messagethread.isRunning():
            time.sleep(1)
    
    
    def testPop(self):
        self.messagethread.push("msg1")
        msg = self.messagethread.pop()
        self.assertTrue(msg == 'msg1')
        t0 = time.clock()
        try:
            self.messagethread.pop(2)
            self.assertTrue(False, "should never be here")
        except MessageEmptyError as e:
            self.assertTrue(time.clock() - t0 > 1.9) 
        
             
    
    def testPush(self):
        self.messagethread.setCapacity(1)
        self.messagethread.push('msg1')
        t0 = time.clock()
        try:
            self.messagethread.push('msg2', 2)
            self.assertTrue(False, "should never be here")
        except MessageFullError as e:
            self.assertTrue(time.clock() - t0 > 1.9)
            
    
    def testStop(self):
        self.messagethread.stop()
        try:
            self.messagethread.push('msg')
            self.assertTrue(False, "should never be here")
        except StopError as e:    
            self.assertTrue(True)
        
        try:
            self.messagethread.pop('msg')
            self.assertTrue(False, "should never be here")
        except StopError as e:
            self.assertTrue(True)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    