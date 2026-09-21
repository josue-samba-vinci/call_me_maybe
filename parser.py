def arg_parser(arg: str) -> bool:
    flags: list[str] = ["--functions_definition",
                        "--input",
                        "--output"]
    if arg not in flags:
        return False
    return True
