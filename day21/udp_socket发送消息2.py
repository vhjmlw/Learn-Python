# -*- coding:utf-8 -*-

'使用UDP-socket持续发送信息'

__author__ = '建磊'

from socket import *

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(('',7788))
    socketAdd = ('192.168.5.105',8080)
    while True:
        msg = input('请输入想要发送的内容：')
        if msg == 'exit' or msg == 'quit':
            break
        udp_socket.sendto(msg.encode('gb2312'),socketAdd)

if __name__ == '__main__':
    main()
