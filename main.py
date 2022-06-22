#!/usr/bin/python3

import socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.10"
port = 444

serverSocket.bind((host, port))
serverSocket.listen(3)

while True:
    clientSocket, address = serverSocket.accept()
    print(f"[*] received connection from {str(address)}")
    message = "Welcome to the server"
    clientSocket.send(message.encode('ascii'))
    clientSocket.close()