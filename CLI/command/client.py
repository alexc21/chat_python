import typer
from typing import Annotated, Optional
from client.client_res import Client
import ipaddress
import os
import json
import psutil

client_app = typer.Typer()

@client_app.command()
def connect_client():
    try:
        with open("process.pid", "r") as file:
            data = json.load(file)
        client = Client(port=data["port"])
        client.connection()
        while True:
            message = input("write your message: ")
            if (message == "exit"):
                client.send_message(message)
                client.cut_connection()
                break
            client.send_message(message)
            response_serv = client.receive_message()
            print(f"response: {response_serv}")
            

    except FileNotFoundError:
        print("no server running")

    