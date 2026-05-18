import typer
from typing import Annotated, Optional
from serveur.server import Server
import ipaddress
import os
import json
import psutil

server_app = typer.Typer()

@server_app.command()
def server_start(
    port: Annotated[Optional[int], typer.Option(help=" need port for server")]= None,
    ip: Annotated[Optional[str], typer.Option(help="need ip address")]= None
):
    if port is not None:
        if port <= 1024:
            raise typer.BadParameter("your port need to be greater than 1024")
        if port > 65535:
            raise typer.BadParameter("your port need to be less than 65535")
    else:
        port = int(os.getenv("PORT", "1025"))

    if ip is not None:
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            raise typer.BadParameter("Invalid ip address")
      
    server = Server(host= ip, port=port)
    server.start_server()
    print("the server listen for a client")
    with open("process.pid", "w") as file:
        json.dump({
            "pid": int(os.getpid()),
            "port": port
        }, file)
    while True:
        client, adresse = server.accept_connection()
        print(f"Client connecté : {adresse}")



@server_app.command()
def server_stop():
    try:
        with open("process.pid", "r") as file:
            data = json.load(file)
        if psutil.pid_exists(data["pid"]) is True:   
            process = psutil.Process(data["pid"]) 
            process.terminate()
            os.remove("process.pid")
        else:
            print("the server not running")
    except FileNotFoundError:
        print("no server is currently running")

    