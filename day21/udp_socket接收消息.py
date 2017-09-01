# -*- coding:utf-8 -*-

'使用UDP—socket接收消息'

__author__ = '建磊'

from socket import *

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(('',7788))
    socketAdd = ('192.168.5.105',8080)
    recvData = udp_socket.recvfrom(1024)
    msg,ip_tuple = recvData
    print('接收到来自于%s的消息：%s'%(str(ip_tuple),msg.decode('gb2312'))) # macos系统默认的编码方式是GB2312
    print('消息来自于')

if __name__ == '__main__':
    main()
