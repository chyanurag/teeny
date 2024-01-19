from lexer import *
from parser import *

def main():
    source = open('code.bs').read()
    lexer = Lexer(source)
    parser = Parser(lexer)
    parser.program()
    print('Parsing completed')
main()
