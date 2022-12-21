TOKENS = set("<>+-[],.")


def parse(code: str):
    return (char for char in code if (char in TOKENS))
# everything that's not in TOKENS is a comment.
