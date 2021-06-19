#!/usr/bin/python3

from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

s = socket(AF_INET, SOCK_STREAM)
host, port = "127.0.0.1", 9999
s.connect((host, port))

print(s.recv(1024))

while True:
    msg = input('> ')
    s.send(msg)
    if msg == "quit":
        break

s.close()
