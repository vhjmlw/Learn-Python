# -*- coding:utf-8 -*-

'单进程非阻塞服务器'

__author__ = '建磊'

from socket import *

def main():
    server_socket = socket(AF_INET,SOCK_STREAM)
    server_socket.bind(('',7788))
    server_socket.setblocking(False)
    server_socket.listen(100)
    socket_list = []
    while True:
        try:
            client_socket,socket_addr = server_socket.accept()
        except:
            pass
        else:
            client_socket.setblocking(False)
            socket_list.append((client_socket,socket_addr))
            print('新连接的客户端：%s'%(str(socket_addr)))

        for client_socket,socket_addr in socket_list:
            try:
                msg = client_socket.recv(1024)
            except:
                pass
            else:
                if len(msg):
                    print('接收到来自%s的信息：%s'%(str(socket_addr),msg.decode('gb2312')))
                else:
                    print('客户端%s关闭'%(str(socket_addr)))
                    client_socket.close()
                    socket_list.remove((client_socket, socket_addr))

if __name__ == '__main__':
    main()
