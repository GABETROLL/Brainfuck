from dataclasses import dataclass
from compilers.python.tokens import TOKENS


@dataclass
class Loop:
    children: list


def parse(token_gen):
    loop_children = []

    while True:
        try:
            token = next(token_gen)
        except StopIteration:
            break

        if token == "]":
            return loop_children
        elif token == "[":
            inside_loop = parse(token_gen)

            loop_children.append(Loop(inside_loop))
        elif token in TOKENS:
            loop_children.append(token)

    return loop_children
