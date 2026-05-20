import typer
from .command.network_cmd import server_app
from .command.client import client_app
from .command.graphical import graphic_interface_app

app = typer.Typer()

app.add_typer(server_app)
app.add_typer(client_app)
app.add_typer(graphic_interface_app)