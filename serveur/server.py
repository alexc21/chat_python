import socket
import os


class Server():
    def __init__(self, host=None, port=None) -> None:
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.host  = host or os.getenv("IP_ADRESSE", "")
        self.port_ = port or int(os.getenv("PORT", "1025"))

    def start_server(self):
        self.socket_.bind((self.host, self.port_ ))
        self.socket_.listen()

    def accept_connection(self):
        return self.socket_.accept()


    def close(self):
        self.socket_.close()


"""
import socket


socket_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_ecoute.bind(('', 1025))
socket_ecoute.listen()

print(socket_ecoute)
print("en attente d'un client")
connex_client, adresse_clien = socket_ecoute.accept()
print(f"connecté a {adresse_clien}")

message = connex_client.recv(1024)
print(f"Recu : {message.decode()}")

connex_client.close()
socket_ecoute.close()

"""

