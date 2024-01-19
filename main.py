from lexer import *

def main():
    source = "LET foobar = 182"
    lexer = Lexer(source)
    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()
main()
