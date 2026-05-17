import typer
from typing import Annotated, Optional
from serveur.server import Network
import ipaddress
import os
import json

app = typer.Typer()

@app.command()
def server_start(
    port: Annotated[Optional[int], typer.Option(help=" need port for server")]= None,
    ip: Annotated[Optional[str], typer.Option(help="need ip address")]= None
):
    if port is not None:
        if port <= 1024:
            raise typer.BadParameter("your port need to be greater than 1024")
        if port > 65535:
            raise typer.BadParameter("your port need to be less than 65535")
        
    if ip is not None:
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            raise typer.BadParameter("Invalid ip address")
      
    server = Network(host= ip, port=port)
    server.start_server()
    print("the server listen for a client")
    with open("process.pid", "w") as file:
        json.dump({
            "pid": os.getpid(),
            "port": port
        }, file)



@app.command()
def server_stop():
    pass