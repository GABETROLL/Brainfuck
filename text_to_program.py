"""Converts output string into the shortest Brainfuck c."""
from math import sqrt

# 'Hi' -> 72, 105
# ++++++++[>+++++++++<-]>.

# [0, 72, 0, 105]


def ascii_codes(output: str):
    """yields ord(char)."""
    for char in output:
        yield ord(char)


def bad(output: str):
    result = ""
    for code in ascii_codes(output):
        result += "+" * code + ">"
    print(result)


def factors_closest_to_square_root(n: int):
    for factor in range(int(sqrt(n)), 1, -1):
        div_result = n / factor
        if div_result % 1 == 0:
            return factor, int(div_result)
    return 1, n


def simplify_signs(sign: str, amount: int):
    # 72 -> 8 * 9 -> 2 * 4 * 3 * 3 -> 2 * 2 * 2 * 3 * 3
    # 2 * 2 * 2 * 3 * 3 -> 2 + 6 + 2 + 6 + 2 + 6 + 3 + 6 + 3 -> 36
    # 4 * 2 * 3 * 3     -> 4 + 6 + 2 + 6 + 3 + 6 + 3         -> 30
    # 2 * 2 * 6 * 3     -> 2 + 6 + 2 + 6 + 6 + 6 + 3         -> 31
    # 2 * 2 * 2 * 9     -> 2 + 6 + 2 + 6 + 2 + 6 + 9         -> 33
    # ...
    # 8 * 9             -> 8 + 6 + 9                         -> 23
    # 8 * 8 + 8         -> 8 + 6 + 1 + 8                     -> 23
    if sign in "<>":
        raise ValueError("IDK how to use those signs...")

    factors = factors_closest_to_square_root(amount)
    return ">" + "+" * factors[0] + "[<" + sign * factors[1] + ">-]"


def main(output: str):
    result = ">"
    for char in output:
        result += simplify_signs("+", ord(char))
    print(result)


def quine_trick(s: str):
    result = ""
    for code in ascii_codes(s):
        result += ">" + "+" * code
    print(result)


print(sorted(((char, ord(char)) for char in "+-<>,.[]"), key=lambda x: x[0]))
