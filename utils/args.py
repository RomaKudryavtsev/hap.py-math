import sympy


def parse_list_from_str(arg_str: str, sym_args: bool | None = False) -> list:
    trimmed = arg_str.replace(" ", "")
    if trimmed.startswith("[") and trimmed.endswith("]"):
        trimmed = trimmed[1:-1]
    splitted = trimmed.split(",")
    return (
        [sympy.sympify(x) for x in splitted]
        if sym_args
        else [float(x) for x in splitted]
    )


def parse_2d_list_from_str(arg_str: str, sym_args: bool | None = False) -> list:
    trimmed = arg_str.replace(" ", "")
    if trimmed.startswith("[") and trimmed.endswith("]"):
        trimmed = trimmed[1:-1]
    splitted = trimmed.split("],")
    return [
        parse_list_from_str(x.replace("[", "").replace("]", ""), sym_args)
        for x in splitted
    ]
