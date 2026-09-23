import sys


def arg_parser() -> dict:
    print(sys.argv)
    relation: dict = {}
    relation = {"--functions_definition": 
                "data/input/functions_definition.json",
                "--input": "data/input/function_calling_tests.json",
                "--output": "data/output/function_calls.json"}
    print(relation)
    if len(sys.argv) > 1:
        contained: list[str] = []
        i: int = 1
        while (i < len(sys.argv)):
            if not flag(sys.argv[i]):
                print(f"{sys.argv[i]} is not an accepted flag")
                return None
            if sys.argv[i] in contained:
                print(f"{sys.argv[i]} is a duplicate")
                return None
            try:
                if flag(sys.argv[i+1]):
                    print("Please put the flags after uv run python3 -m src")
                    print("--functions_definition <function_definition_file>")
                    print("--input <input_file>")
                    print("--output <output_file>")
                    return None
                else:
                    relation[sys.argv[i]] = sys.argv[i+1]
            except IndexError:
                print("At least one flag doesn't have a value attached to it")
                return None
            contained.append(sys.argv[i])
            i += 2
    print(relation)
    return relation


def flag(arg: str) -> bool:
    flags: list[str] = ["--functions_definition",
                        "--input",
                        "--output"]
    if arg not in flags:
        return False
    return True
