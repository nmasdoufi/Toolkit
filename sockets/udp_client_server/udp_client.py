from socket import *
import sys

buffer = 4096
address = ('127.0.0.1', 1337)

client_socket = socket(AF_INET, SOCK_DGRAM)

while(1):
    message = input(">>> ").strip()
    if message == "exit":
        break
    client_socket.sendto(message, address)
    response, addr = client_socket.recvfrom(buffer)
    print("--> " + response)
