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


@matrix_commands.command("multiply")
def multiply_matrices(
    matrix_a: Annotated[
        str, typer.Argument(help="Use format: [[1,2,3],[4,0,6],[7,8,9]]")
    ],
    matrix_b: Annotated[str, typer.Argument(help="Use format: [[1,2],[3,4],[5,6]]")],
    sym_args: Annotated[bool, typer.Option(help="Use symbolic arguments")] = False,
    sym_res: Annotated[bool, typer.Option(help="Use symbolic calculation")] = True,
):
    parsed_a = args_utils.parse_2d_list_from_str(matrix_a, sym_args)
    parsed_b = args_utils.parse_2d_list_from_str(matrix_b, sym_args)
    result = matrix_funcs.multiply(parsed_a, parsed_b, sym_res)
    print(
        f"[bold green]Matrix A:[/bold green] {matrix_a}\n"
        f"[bold green]Matrix B:[/bold green] {matrix_b}\n"
        f"[bold yellow]Result:[/bold yellow] {result} :smile:"
    )


@matrix_commands.command("sum")
def sum_matrices(
    matrix_a: Annotated[
        str, typer.Argument(help="Use format: [[1,2,3],[4,0,6],[7,8,9]]")
    ],
    matrix_b: Annotated[str, typer.Argument(help="Use format: [[1,2],[3,4],[5,6]]")],
    sym_args: Annotated[bool, typer.Option(help="Use symbolic arguments")] = False,
    sym_res: Annotated[bool, typer.Option(help="Use symbolic calculation")] = True,
):
    parsed_a = args_utils.parse_2d_list_from_str(matrix_a, sym_args)
    parsed_b = args_utils.parse_2d_list_from_str(matrix_b, sym_args)
    result = matrix_funcs.sum(parsed_a, parsed_b, sym_res)
    print(
        f"[bold green]Matrix A:[/bold green] {matrix_a}\n"
        f"[bold green]Matrix B:[/bold green] {matrix_b}\n"
        f"[bold yellow]Result:[/bold yellow] {result} :smile:"
    )


@matrix_commands.command("subtract")
def subtract_matrices(
    matrix_a: Annotated[
        str, typer.Argument(help="Use format: [[1,2,3],[4,0,6],[7,8,9]]")
    ],
    matrix_b: Annotated[str, typer.Argument(help="Use format: [[1,2],[3,4],[5,6]]")],
    sym_args: Annotated[bool, typer.Option(help="Use symbolic arguments")] = False,
    sym_res: Annotated[bool, typer.Option(help="Use symbolic calculation")] = True,
):
    parsed_a = args_utils.parse_2d_list_from_str(matrix_a, sym_args)
    parsed_b = args_utils.parse_2d_list_from_str(matrix_b, sym_args)
    result = matrix_funcs.subtract(parsed_a, parsed_b, sym_res)
    print(
        f"[bold green]Matrix A:[/bold green] {matrix_a}\n"
        f"[bold green]Matrix B:[/bold green] {matrix_b}\n"
        f"[bold yellow]Result:[/bold yellow] {result} :smile:"
    )
