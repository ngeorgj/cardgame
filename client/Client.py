#
# // Repositories
#    github@ngeorgj
# 

# imports
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (socket.gethostname(), 23342)
print(f'connecting to {server_address}')
sock.connect(server_address)

while True:
    data = sock.recv(1024)
    print(f'{data.decode("utf-8")}')

    if not data:
        socket.close()