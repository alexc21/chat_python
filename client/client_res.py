import socket

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connexion_serveur.connect(('127.0.0.1', 1025))

connexion_serveur.send("Hello world".encode())
connexion_serveur.close()