from lex import *

def main():
    source = 'LET foo = 123'
    lexer = Lexer(source)

    tok = lexer.getToken()
    while tok.kind != TokenType.EOF:
        print(tok.kind)
        tok = lexer.getToken()

main()
