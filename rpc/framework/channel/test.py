'''
Created on 2015年8月3日

@author: sunshyran
'''
from framework.channel.SocketChannel import SocketChannelAcceptor


if __name__ == '__main__':
    accepter = SocketChannelAcceptor('127.0.0.1', 12345)
    while True:
        channel = accepter.accept()
        print(channel)