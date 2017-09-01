# -*- coding:utf-8 -*-


'创建一个客户端TCP-socket'

__author__ = '建磊'

from socket import *
from threading import Thread

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(('192.168.5.105',7788))

def main():
    def sendMsg():
        while True:
            msg = input('请输入要发送的信息：')
            if msg:
                client_socket.send(msg.encode('gb2312'))

    def recvMsg():
        while True:
            msg = client_socket.recv(1024)
            if msg:
                print('接收到信息：%s'%(msg.decode('gb2312')))

    th1 = Thread(target=sendMsg)
    th2 = Thread(target=recvMsg)
    th1.start()
    th2.start()

if __name__ == '__main__':
    main()
