# -*- coding:utf-8 -*-

'UDP-socket多线程接信息发信息'

__author__ = '建磊'

from socket import *
from threading import Thread

def main():

    def sendMsg(udp_socket,socketAddr):
        while True:
            msg = input('请输入要发送的信息：')
            udp_socket.sendto(msg.encode('gb2312'),socketAddr)

    def recvMsg(udp_socket,):
        while True:
            recvData = udp_socket.recvfrom(1024)
            print('接收到来自%s的信息：%s'%(str(recvData[1]),recvData[0].decode('gb2312')))

    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(('',7788))
    socketAddr = ('192.168.5.105',8080)
    th1 = Thread(target=sendMsg,args=(udp_socket,socketAddr))
    th2 = Thread(target=recvMsg,args=(udp_socket,))
    th1.start()
    th2.start()

if __name__ == '__main__':
    main()
