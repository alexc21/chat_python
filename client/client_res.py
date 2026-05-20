import socket
import os


class Client():
    def __init__(self, host=None, port=None) -> None:
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.host  = host or os.getenv("IP_ADRESSE_CLIENT", "127.0.0.1")
        self.port_ = port or int(os.getenv("PORT", "1025"))

    def connection(self):
        self.socket_.connect((self.host, self.port_))

    def cut_connection(self):
        self.socket_.close()

    def send_message(self, message):
        self.socket_.send(message.encode())

    def receive_message(self):
        return self.socket_.recv(1024).decode()

