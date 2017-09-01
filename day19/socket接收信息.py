# -*- coding:utf-8 -*-

'使用socket接收信息'

__authro__ = '建磊'

from socket import *

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(('',7788))
    print('nima')
    #recvfrom()的执行是阻塞式的，代码会停留在这个位置，不会往下执行，直到接收到信息
    udp_socket.recvfrom(1024)
    print('wo cao')
    udp_socket.sendto(b'helloworld',('192.168.1.5',8080))

if __name__ == '__main__':
    main()
