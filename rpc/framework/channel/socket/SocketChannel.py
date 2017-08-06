'''
Created on 2015年8月3日

@author: sunshyran
'''
import socket

from rpc.framework.channel.Acceptor import AbstractChannelAccepter
from rpc.framework.channel.Channel import AbstractChannel
from rpc.framework.channel.Connector import AbstractChannelConnector
from rpc.framework.channel.ChannelError import ChannelBrokenError


class SocketChannel(AbstractChannel):
    '''
    a channel realization base on socket.
    '''


    def __init__(self, socket,addr):
        '''
        Constructor
        '''
        super().__init__()
        self.socket = socket
        self.addr = addr
      
        
    def send(self, data):
        '''
        send data until all is sent. If error occurred, raise Exception
        @param data: 字节串
        '''
        try:
            #print('send', bytes(data, encoding = "utf8"))
            self.socket.sendall(data)
        except socket.error as e:
            raise ChannelBrokenError(str(e))
    
    
    def recv(self):
        '''
        recv data. if error occurred, raise Exception
        '''
        try:
            s = self.socket.recv(32*1024)
            #print('recv', s)
            return s
        except socket.error as e:
            raise ChannelBrokenError(str(e))
    
    
    def close(self):
        '''
        close channel
        '''
        print('channel %s is closed' % str(self.addr))
        return self.socket.close()
    
    
    def __str__(self):
        return str(self.socket) + str(self.addr)
    


class SocketChannelConnector(AbstractChannelConnector):
       
       
    def __init__(self, host, port):
        '''
        Constructor
        '''
        super().__init__()
        self._host = host
        self._port = port
    
    
    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self._host, self._port))
        return SocketChannel(s, s.getsockname())

    
    
class SocketChannelAcceptor(AbstractChannelAccepter):
    def __init__(self, host, port):
        '''
        Constructor
        '''
        super().__init__()
        self._host = host
        self._port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self._host, self._port))
        self.sock.listen(5)


    def accept(self):
        conn, addr = self.sock.accept()
        return SocketChannel(conn, addr)
    
    
    def interrupt(self):
        self.sock.close()
            
        
        
if __name__ == '__main__':
    conn = SocketChannelConnector('127.0.0.1', 12345).connect()
    print(conn)
    
    