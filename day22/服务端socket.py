# -*- coding:utf-8 -*-

'创建一个服务端TCP-socket'

__author__ = '建磊'

from socket import *
from threading import Thread

def main():
    server_socket = socket(AF_INET,SOCK_STREAM)
    server_socket.bind(('',7788))
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.listen(1000)
    while True:
       client_socket,socketAddr = server_socket.accept()
       while True:
        msg = client_socket.recv(1024)
        print('接收到来自%s的信息：%s'%(str(socketAddr),msg.decode('gb2312')))
        tmp = input('请输入要发送给客户端的信息')
        client_socket.send(tmp.encode('gb2312'))


if __name__ == '__main__':
    main()