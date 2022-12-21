import argparse
from compilers.python import tokens
import AST
from write import write_as_python
from write import write_as_assembly


def main(input_path: str, output_path: str):
    if not output_path.endswith(".py") and not output_path.endswith(".asm"):
        raise ValueError("Must compile to Python (.py) or x86 Linux Assembly (.asm).")

    with open(input_path) as bf:
        code = bf.read()

    code_tokens = tokens.parse(code)
    ast = AST.parse(code_tokens)
    if output_path.endswith(".py"):
        write_as_python(output_path, ast)
    elif output_path.endswith(".asm"):
        write_as_assembly(output_path, ast)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file", help="brainfuck file to compile")
    arg_parser.add_argument("path", help="(folder) path to compile to")
    args = arg_parser.parse_args()

    main(args.file, args.path)
