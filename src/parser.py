class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def consume(self, expected_kind):
        kind, val = self.tokens[self.pos]
        if kind == expected_kind:
            self.pos += 1
            return val
        raise SyntaxError(f"Expected {expected_kind}, got {kind}")

    def parse(self):
        statements = []
        while self.peek()[0] != "EOF" and self.peek()[0] != "RBRACE":
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        kind, val = self.peek()
        if kind == "YAAD_RAKH":
            self.consume("YAAD_RAKH")
            var_name = self.consume("ID")
            self.consume("ASSIGN")
            expr = self.parse_expression()
            return ("ASSIGN", var_name, expr)
        elif kind == "DIKHAO":
            self.consume("DIKHAO")
            return ("PRINT", self.parse_expression())
        elif kind == "JAB_TAK":
            self.consume("JAB_TAK")
            cond = self.parse_expression()
            self.consume("LBRACE")
            body = self.parse()
            self.consume("RBRACE")
            return ("WHILE", cond, body)
        elif kind == "AGAR":
            self.consume("AGAR")
            cond = self.parse_expression()
            self.consume("LBRACE")
            if_body = self.parse()
            self.consume("RBRACE")
            else_body = None
            if self.peek()[0] == "VARNA":
                self.consume("VARNA")
                self.consume("LBRACE")
                else_body = self.parse()
                self.consume("RBRACE")
            return ("IF", cond, if_body, else_body)
        self.pos += 1  # Safety skip
        return None

    def parse_expression(self):
        expr_tokens = []
        stop_tokens = ("LBRACE", "RBRACE", "EOF", "DIKHAO", "YAAD_RAKH", "JAB_TAK", "AGAR", "VARNA")
        while self.peek()[0] not in stop_tokens:
            expr_tokens.append(self.tokens[self.pos][1])
            self.pos += 1
        return " ".join(expr_tokens)
