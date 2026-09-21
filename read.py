import sys
import typing

def read_file() -> None:
    if len(sys.argv) == 1:
        try:
            f: typing.IO[str] = open(f"{/data/function_calling_tests.json}", "r")
        except OSError as e:
            print(f"Error opening the file '/data/function_calling_tests.json' : {e}")
        try:
            content = f.read
        except (UnicodeDecodeError, Exception, BaseException) as e:
            print(f"Error reading the file '/data/function_calling_tests.json' : {e}")
    
