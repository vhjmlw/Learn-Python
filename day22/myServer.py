# -*- coding:utf-8 -*-

'创建一个简洁版的服务器，能够处理http请求并响应'

__author__ = '建磊'

from socket import *
from multiprocessing import Process

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',7788))
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.listen()

def fn(client, addr):
    while True:
        msg = client.recv(1024)
        if msg:
            new_msg = msg.decode('gb2312')
            print('接收到%s的信息：%s'%(str(addr), new_msg))
            #对获取到的请求报文进行解析
            new_list = new_msg.split('\\r\\n')
            print(new_list)
        response = r"""
            HTTP/1.1 200 OK
            Content-Type: application/html
            Connection: keep-alive
            
            hello world
        """
        response = 'HTTP/1.1 200 OK\r\nServer:my server\r\n\r\nhelloworld'
        client.send(bytes(response, 'utf-8'))
        client.close()

def main():
    while True:
        client_socket,socket_addr = server_socket.accept()
        proc = Process(target=fn, args=(client_socket, socket_addr))
        proc.start()
        client_socket.close()#记得要将client_socket关闭，新创建的进程中已经拷贝了一份

if __name__ == '__main__':
    main()