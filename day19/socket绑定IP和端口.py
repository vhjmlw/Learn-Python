# -*- coding:utf-8 -*-

'绑定socket的IP和端口'

__author__ = '建磊'

from socket import *

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    ip_port = ('',7788)
    udp_socket.bind(ip_port)
    udp_socket.sendto(b'hello world',('192.168.1.5',8080))

if __name__ == '__main__':
    main()
