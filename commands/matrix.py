import typer
from typing_extensions import Annotated
from rich import print
from funcs import matrix_funcs
from utils import args_utils


matrix_commands = typer.Typer()


@matrix_commands.command("determinant")
def calc_determinant(
    matrix: Annotated[
        str, typer.Argument(help="Use format: [[1,2,3],[4,0,6],[7,8,9]]")
    ],
    sym_args: Annotated[bool, typer.Option(help="Use symbolic arguments")] = False,
    sym_res: Annotated[bool, typer.Option(help="Use symbolic calculation")] = True,
):
    parsed = args_utils.parse_2d_list_from_str(matrix, sym_args)
    result = matrix_funcs.determinant(parsed, sym_res)
    print(
        f"[bold green]Matrix:[/bold green] {matrix}\n[bold yellow]Determinant:[/bold yellow] {result} :smile:"
    )
