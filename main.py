from lexer import *

def main():
    source = "--this is something random\n +-*/ *-\n -- this is something extra "
    lexer = Lexer(source)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()
main()
