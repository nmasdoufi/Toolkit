from socket import *
import sys

buffer = 4096

address = ('127.0.0.1', 1337)
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(address)

while(1):
    print("Listening ...")
    recv_data, addr = server_socket.recvfrom(buffer)
    recv_data = recv_data.strip()
    print(f"Recieved from: {addr}\nMessage: {recv_data}")
    try:
        response = sys.platform
    except Exception as e:
        response = sys.exc_info()[0] # Return information about the most recent exception caught by an except clause
    print("Response: " + response)
    server_socket.sendto(response, addr)

server_socket.close()
