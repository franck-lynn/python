from socket import *
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpClientSocket = socket(AF_INET, SOCK_STREAM)
tcpClientSocket.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpClientSocket.send(bytes(data, 'utf-8'))
    data = tcpClientSocket.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpClientSocket.close()
# python Client.py

