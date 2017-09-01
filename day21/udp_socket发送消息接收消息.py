# -*- coding:utf-8 -*-

'使用UDP-socket发送消息和接收消息'

__author__ = '建磊'

from socket import *

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(('',7788))
    socketAddr = ('192.168.5.105',8080)
    while True:
        msg = input('请输入要发送的信息。。。')
        if msg == 'exit' or msg == 'quit':
            break
        udp_socket.sendto(msg.encode('gb2312'),socketAddr)
        recvData = udp_socket.recvfrom(1024)
        print('接收到%s的信息：%s'%(str(recvData[1]),recvData[0].decode('gb2312')))

if __name__ == '__main__':
    main()
