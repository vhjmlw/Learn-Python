# -*- coding:utf-8 -*-

'使用UDP-socket持续的接收消息'

__author__ = '建磊'

from socket import *

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(('',7788))
    docketAddr = ('192.168.5.105',8080)
    while True:
       recvData = udp_socket.recvfrom(1024)
       print('>>接收到%s的信息：%s'%(str(recvData[1]),recvData[0].decode('gb2312')))

if __name__ == '__main__':
    main()
