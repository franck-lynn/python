from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
# 创建一个服务器端套接字, addredd_family, AF
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(ADDR)
tcpServerSocket.listen(5)

while True:
    print("等待连接...")
    tcpClientSocket, addr = tcpServerSocket.accept()
    print('...来自' + str(addr) + "的连接")
    while True:
        data = tcpClientSocket.recv(BUFSIZ)
        if not data:
            break
        # tcpClientSocket.send(bytes(ctime(), 'utf-8'))
        # tcpClientSocket.send(bytes('给客户端带句话', 'utf-8'))
        tcpClientSocket.send(bytes('[%s] %s' % (ctime() , data), 'utf-8'))
        
    tcpClientSocket.close()
tcpServerSocket.close()
# python server.py


