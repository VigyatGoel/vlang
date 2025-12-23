# vlang - A Hindi-English Programming Language

vlang is a fun experimental programming language that blends Hindi and English syntax. Created as a hobby project to explore language design and implementation. Built with Python, it features a custom lexer, parser, and interpreter.

**Why "vlang"?** Named after my name, Vigyat, which starts with 'V'.

## Features

- **Bilingual Syntax**: Combines Hindi keywords with English-style programming constructs
- **Variable Declaration**: `yaad rakh` (remember) for variable assignment
- **Output**: `dikhao` (show) for printing values
- **Conditionals**: `agar` (if) and `varna` (else) for decision-making
- **Loops**: `jab tak` (while/until) for iteration
- **Expressions**: Support for arithmetic operations and comparisons
- **Clean Architecture**: Modular design with separate lexer, parser, and interpreter

## Installation

### Prerequisites
- Python 3.12 or higher
- uv (recommended) or pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/VigyatGoel/vlang.git
cd vlang
```

2. Install dependencies (if any):
```bash
uv sync
```

## Syntax Guide

### Variable Declaration
Use `yaad rakh` (remember) to declare and assign variables:

```vlang
yaad rakh x = 10
yaad rakh name = "Vigyat"
yaad rakh price = 99.99
```

### Output
Use `dikhao` (show) to print values:

```vlang
dikhao "Hello, World!"
dikhao x
dikhao x + 5
```

### Conditionals
Use `agar` (if) and `varna` (else) for conditional statements:

```vlang
yaad rakh age = 18

agar age >= 18 {
    dikhao "Adult"
} varna {
    dikhao "Minor"
}
```

The `varna` (else) block is optional:

```vlang
agar score > 50 {
    dikhao "Pass!"
}
```

### Loops
Use `jab tak` (while/until) for loops:

```vlang
yaad rakh count = 1
yaad rakh max = 5

jab tak count < max {
    dikhao count
    yaad rakh count = count + 1
}
```

### Expressions
vlang supports standard arithmetic and comparison operators:

- Arithmetic: `+`, `-`, `*`, `/`
- Comparison: `>`, `<`, `>=`, `<=`, `==`, `!=`

```vlang
yaad rakh result = 10 + 5 * 2
yaad rakh is_greater = result > 15
```

## Usage

Run a vlang program using:

```bash
uv run src/vlang.py <filename>.vlang
```

### Example

Create a file `example.vlang`:

```vlang
yaad rakh x = 10
yaad rakh y = 20

dikhao "Starting calculation..."

agar x < y {
    dikhao "x is smaller"
    yaad rakh result = y - x
    dikhao result
} varna {
    dikhao "x is greater or equal"
}

dikhao "Done!"
```

Run it:

```bash
uv run src/vlang.py example.vlang
```

## Project Structure

```
vlang/
├── src/
│   ├── vlang.py          # Main entry point
│   ├── lexer.py          # Tokenizer
│   ├── parser.py         # Syntax parser (AST builder)
│   ├── interpreter.py    # Runtime executor
│   └── token_spec.py     # Token definitions
├── hello.vlang           # Sample loop program
├── if_else.vlang         # Sample conditional program
├── pyproject.toml        # Project metadata
└── README.md             # This file
```

## Examples

### Example 1: Hello World
```vlang
dikhao "Hello, World!"
```

### Example 2: Counter
```vlang
yaad rakh count = 1
yaad rakh max = 4

jab tak count < max {
    dikhao "Iteration:"
    dikhao count
    yaad rakh count = count + 1
}
```

### Example 3: Grade Calculator
```vlang
yaad rakh marks = 75

agar marks >= 90 {
    dikhao "Grade: A"
} varna {
    agar marks >= 75 {
        dikhao "Grade: B"
    } varna {
        agar marks >= 60 {
            dikhao "Grade: C"
        } varna {
            dikhao "Grade: F"
        }
    }
}
```

## Keywords Reference

| Hindi Keyword | English Meaning | Purpose |
|--------------|-----------------|---------|
| `yaad rakh` | remember | Variable declaration/assignment |
| `dikhao` | show | Print/output statement |
| `agar` | if | Conditional statement |
| `varna` | else/otherwise | Else clause |
| `jab tak` | while/until | While loop |

## Technical Details

### Architecture

vlang uses a three-phase compilation process:

1. **Lexical Analysis (Lexer)**: Converts source code into tokens
2. **Parsing (Parser)**: Builds an Abstract Syntax Tree (AST) from tokens
3. **Interpretation (Interpreter)**: Executes the AST

### Implementation

- **Language**: Python 3.12+
- **Pattern Matching**: Regular expressions for tokenization
- **Execution**: Direct AST interpretation with Python's `eval()` for expressions

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Add more Hindi keywords
- Improve documentation

## Roadmap

Potential future features:
- [ ] Functions (`kaam` - work/task)
- [ ] Arrays/Lists
- [ ] Comments support
- [ ] For loops (`har ek` - for each)
- [ ] Better error messages
- [ ] Type system
- [ ] Standard library
- [ ] REPL mode

## Author

Vigyat Goel

## Acknowledgments

Built as a fun side project exploring language design.

---

**Note**: This is a hobby project made for fun and learning about compilers and interpreters.