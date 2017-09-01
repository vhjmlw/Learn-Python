# -*- coding:utf-8 -*-

'创建UDP—socket套接字'

__author__ = '建磊'

from socket import *

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(('',7788)) #bind方法传入的是一个元组
    socketAdd = ('192.168.5.105',8080)
    udp_socket.sendto(b'hello world',socketAdd)
    udp_socket.close()

if __name__ == '__main__':
    main()
