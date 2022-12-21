from compilers.python.AST import Loop


def instruction(ast_item, tabs=0):
    if ast_item == "+":
        return "    " * tabs + "data[pointer] += 1\n"
    elif ast_item == "-":
        return "    " * tabs + "data[pointer] -= 1\n"
    elif ast_item == "<":
        return "    " * tabs + "pointer -= 1\n"
    elif ast_item == ">":
        return "    " * tabs + "pointer += 1\n"
    elif ast_item == ".":
        return "    " * tabs + "print(chr(data[pointer]), end='')\n"
    elif ast_item == ",":
        return "    " * tabs + "data[pointer] = ord(input('>>>'))\n"
    elif isinstance(ast_item, Loop):
        result = "    " * tabs + "while data[pointer] != 0:\n"

        if not ast_item.children:
            result += "    " * (tabs + 1) + "pass"
            return result
        # Empty loop needs pass in Python.

        for loop_item in ast_item.children:
            result += instruction(loop_item, tabs + 1)

        return result
    else:
        s = f"{ast_item} is not valid."
        raise ValueError(s)


def write(path: str, ast: list):
    if not path.endswith(".py"):
        raise ValueError("Must be .py file.")

    with open(path, "w") as file:
        with open("write/write_python/format.txt") as assembly_format:
            file.write(assembly_format.read())

        for i in ast:
            file.write(instruction(i))
