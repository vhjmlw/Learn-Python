# -*- coding:utf-8 -*-

'使用socket发送消息'

__author__= '建磊'

from socket import *

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.sendto(b'hello world',('192.168.1.5',8080))

if __name__ == '__main__':
    main()
