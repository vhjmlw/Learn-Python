# -*- coding:utf-8 -*-

'实现聊天室'

__author__ = '建磊'

from socket import *
from threading import Thread

udp_socket = socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(('',7788))
ip = input('请输入IP地址')
port = int(input('请输入端口号'))

def main():
    def receive():
        while True:
            tmp = input('<<')
            udp_socket.sendto(tmp.encode('utf-8'),(ip,port))

    def send():
        while True:
           recvData =  udp_socket.recvfrom(1024)
           print('>>%s:%s'%(str(recvData[1]),recvData[0]))

    th1 = Thread(target=receive)
    th2 = Thread(target=send)
    th1.start()
    th2.start()
    th1.join()
    th2.join()

if __name__ == '__main__':
    main()
