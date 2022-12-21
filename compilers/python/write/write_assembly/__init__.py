from compilers.python.AST import Loop


loops = 0


def instruction(ast_item):
    global loops

    if ast_item == "+":
        return "\tadd [rsp], byte 1\n"
    elif ast_item == "-":
        return "\tsub [rsp], byte 1\n"
    elif ast_item == "<":
        return "\tdec rsp\n"
    elif ast_item == ">":
        return "\tinc rsp\n"
    elif ast_item == ".":
        return "\tcall print\n"
    elif ast_item == ",":
        return "\tcall input\n"
    elif isinstance(ast_item, Loop):
        result = f"\tjmp loop{loops}\n" + f"loop{loops}:\n"

        result += f"\tcmp [rsp], byte 0\n"
        result += f"\tje end_loop{loops}\n"

        for loop_item in ast_item.children:
            result += instruction(loop_item)

        result += f"\tjmp loop{loops}\n"
        result += f"end_loop{loops}:\n"

        loops += 1

        return result
    else:
        s = f"{ast_item} is not valid."
        raise ValueError(s)


def write(path: str, ast: list):
    if not path.endswith(".asm"):
        raise ValueError("Must be .asm file.")

    with open(path, "w") as file:
        with open("write/write_assembly/format.txt") as assembly_format:
            file.write(assembly_format.read())

        for i in ast:
            file.write(instruction(i))

        file.write("\tjmp exit")
