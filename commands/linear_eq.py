import typer
from typing_extensions import Annotated
from rich import print
from funcs import linear_eq_funcs
from utils import args_utils

linear_eq_commands = typer.Typer()


@linear_eq_commands.command("solve")
def solve_linear_system(
    equations_sys: Annotated[
        str, typer.Argument(help="Use format: [[1,2,3],[4,0,6],[7,8,9]]")
    ],
    sym_res: Annotated[bool, typer.Option(help="Use symbolic calculation")] = True,
):
    parsed = args_utils.parse_2d_list_from_str(equations_sys)
    result = linear_eq_funcs.solve_linear_system(parsed, sym_res)
    print(
        f"[bold green]Equations system:[/bold green] {equations_sys}\n"
        f"[bold yellow]Solution:[/bold yellow] {result} :smile:"
    )
