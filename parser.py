import sys


def arg_parser() -> dict:
    #print(sys.argv)
    relation: dict = {}
    relation = {"--functions_definition": 
                "data/input/functions_definition.json",
                "--input": "data/input/function_calling_tests.json",
                "--output": "data/output/function_calls.json"}
    #print(relation)
    if len(sys.argv) > 2:
        contained: list[str] = []
        i: int = 2
        while (i < len(sys.argv)):
            if sys.argv[i] in contained:
                print("please put each flag only once")
            if not flag(sys.argv[i]):
                print(f"{sys.argv[i]} is not an accepted flag")
                print("Please put the flags after uv run python3 -m src")
                print("--functions_definition <function_definition_file>")
                print("--input <input_file>")
                print("--output <output_file>")
        
            else:
                i += 1
                try:
                    if not flag(sys.argv[i]):
                        relation[sys.argv[i-1]] = sys.argv[i]
                    else:
                        print("one of your values is a flag")
                        return None
                except IndexError:
                    print("At least one flag doesn't have a value attached to it")
                    return None
                contained.append(sys.argv[i-1])
                i += 1
    #print(relation)
    return relation


def flag(arg: str) -> bool:
    flags: list[str] = ["--functions_definition",
                        "--input",
                        "--output"]
    if arg not in flags:
        return False
    return True


if __name__ == "__main__":
    arg_parser()
