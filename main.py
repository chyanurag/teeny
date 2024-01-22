from lex import *
from emit import *
from parse import *
import sys

def main():
    print("Teeny tiny compiler")

    if len(sys.argv) != 2:
        sys.exit("filename required")
    with open(sys.argv[1], "r") as f:
        source = f.read()

    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program()
    emitter.writeFile()
    print("Compiling completed")

main()
