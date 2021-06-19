#!/usr/bin/python3

"""
    This server socket will open a TCP socket on localhost:9999, and listens
to request in an infinite loop. When a request is received, it will return a
message indicating that a connection has been established.

"""
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

ip, port = "localhost", 1337

server = socket(AF_INET, SOCK_STREAM)
server.bind((ip, port))
server.listen(5)

print(f"[*] Listening on {ip}:{port} ...")

# This is gonna be our client-handling thread
def client_handling_thread(client_socket):
    # Printing out what the client sends
    response = client_socket.recv(1024)
    print("[+] Received request : %s" %response)
    client_socket.send("Message Received")
    client_socket.close()

while True:
    client, address = server.accept()
    print(f"[+] Connection Accepted from {address[0]}:{address[1]}")

    client_handler = Thread(target=client_handling_thread, args=(client,))
    client_handler.start()
