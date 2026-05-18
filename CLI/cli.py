import typer
from .command.network_cmd import server_app

app = typer.Typer()

app.add_typer(server_app)