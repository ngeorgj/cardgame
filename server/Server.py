#
# // Repositories
#    github@ngeorgj
# 

# imports

import socket
import socketserver


class GameServer(socketserver.StreamRequestHandler):
    ip_address = socket.gethostname()
    port = 23342

    active_connections = []

    def handle(self) -> None:
        pass
