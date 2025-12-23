import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vlang.py <filename>.vlang")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, "r") as f:
            source_code = f.read()

        lexer = Lexer(source_code)
        parser = Parser(lexer.tokens)
        ast = parser.parse()
        interp = Interpreter()
        interp.run(ast)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
