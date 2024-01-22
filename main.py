from lex import *
from parse import *
import sys

def main():
    print("Teeny tiny compiler")
    if len(sys.argv) != 2:
        sys.exit("filename required")
    with open(sys.argv[1], "r") as f:
        source = f.read()
    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program()
    print("Parsing completed")

main()
