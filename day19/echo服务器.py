# -*- coding:utf-8 -*-

'echo服务器'

__author__ = '建磊'

from socket import *

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(('',7788))
    recvData = udp_socket.recvfrom(1024)
    print(str(recvData))
    udp_socket.sendto(recvData[0].encode('utf-8'),recvData[1])

if __name__ == '__main__':
    main()
