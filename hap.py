import typer
from commands import linear_eq_commands, matrix_commands

app = typer.Typer()
app.add_typer(linear_eq_commands, name="linear_eq")
app.add_typer(matrix_commands, name="matrix")

if __name__ == "__main__":
    app()
