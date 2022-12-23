code: str = input()
data = [0] * 30
pointer = 0


def parse(index) -> int:
    global pointer

    while index < len(code):
        if code[index] == "+":
            data[pointer] += 1
        if code[index] == "-":
            data[pointer] -= 1
        if code[index] == ">":
            pointer += 1
        if code[index] == "<":
            pointer -= 1
        if code[index] == ".":
            print(chr(data[pointer]), end="")
        if code[index] == ",":
            data[pointer] = ord(input())
        if code[index] == "[":
            new_index = index

            while data[pointer]:
                new_index = parse(index + 1)

            index = new_index
        elif code[index] == "]":
            return index
        index += 1
    return index


parse(0)
