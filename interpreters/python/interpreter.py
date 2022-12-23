import argparse

array = bytearray(200)
p = 0


def chars_until_closing_bracket(code_iter):
    result = ""
    open_count = 1
    while True:
        try:
            char = next(code_iter)
        except StopIteration:
            raise SyntaxError("No closing bracket")
        if char == "[":
            open_count += 1
        elif char == "]":
            open_count -= 1

            if open_count == 0:
                return result

        result += char


def interpret(code_iter):
    global p

    while True:
        try:
            char = next(code_iter)
        except StopIteration:
            break

        if char == "<":
            pointer -= 1
        elif char == ">":
            pointer += 1
        elif char == "-":
            if array[pointer] == 0:
                array[pointer] = 255
            else:
                array[pointer] -= 1
        elif char == "+":
            if array[pointer] == 255:
                array[pointer] = 0
            else:
                array[pointer] += 1
        elif char == ".":
            print(chr(array[pointer]), end="")
        elif char == ",":
            input_string = input("")
            if input_string:
                array[pointer] = ord(input_string[0])
            else:
                array[pointer] = 0
        elif char == "[":
            loop_chars = chars_until_closing_bracket(code_iter)

            while array[pointer] != 0:
                loop_iter = iter(loop_chars)

                interpret(loop_iter)
        elif char == "]":
            raise SyntaxError("Unexpected bracket.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File path and name to interpret.")
    args = parser.parse_args()

    with open(args.file) as file:
        code_iter = iter(file.read())

    interpret(code_iter)


if __name__ == "__main__":
    main()
