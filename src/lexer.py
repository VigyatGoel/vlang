import re
from token_spec import TOKEN_SPEC


class Lexer:
    def __init__(self, code):
        self.tokens = []
        tok_regex = "|".join("(?P<%s>%s)" % pair for pair in TOKEN_SPEC)
        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            val = mo.group()
            if kind == "SKIP":
                continue
            elif kind == "MISMATCH":
                raise RuntimeError(f"Syntax Error: Unexpected character {val}")
            self.tokens.append((kind, val))
        self.tokens.append(("EOF", None))
