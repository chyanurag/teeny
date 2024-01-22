import enum
import sys

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    CCODE = 4
    # Keywords.
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111

    #Custom keywords
    PRINTLN = 112
    # Operators.
    EQ = 201  
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211

class Token:
    def __init__(self, text, kind):
        self.kind = kind
        self.text = text
    
    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            if kind.name == tokenText and kind.value >= 100 and kind.value < 200:
                return kind

        return None

class Lexer:
    def __init__(self, source):
        self.source = source + '\n'
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]

    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]

    def abort(self, message):
        sys.exit("lexing error : " + message)

    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    def skipComment(self):
        if self.curChar == '#':
            self.nextChar()
            while self.curChar != '\n':
                self.nextChar()

    def getToken(self):
        self.skipWhitespace()
        self.skipComment()
        tok = None
        if self.curChar == '+':
            tok = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            tok = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            tok = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            tok = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '\n':
            tok = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar == '\0':
            tok = Token('', TokenType.EOF)
        elif self.curChar == '=':
            if self.peek() == '=':
                self.nextChar()
                tok = Token('==', TokenType.EQEQ)
            else:
                tok = Token('=', TokenType.EQ)
        elif self.curChar == '`':
            startPos = self.curPos
            self.nextChar()
            while self.curChar != '`':
                self.nextChar()
            tok = Token(self.source[startPos + 1 : self.curPos], TokenType.CCODE)

        elif self.curChar == '>':
            if self.peek() == '=':
                self.nextChar()
                tok = Token('>=', TokenType.GTEQ)
            else:
                tok = Token('>', TokenType.GT)
        elif self.curChar == '<':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                tok = Token(lastChar + self.curChar, TokenType.LTEQ)
            else:
                tok = Token(self.curChar, TokenType.LT)
        elif self.curChar == '!':
            if self.peek() == '=':
                self.nextChar()
                tok = Token('!=', TokenType.NOTEQ)
            else:
                self.abort("expected != got " + self.peek())
        

        elif self.curChar == '\"':
            self.nextChar()
            startPos = self.curPos
            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '%' or self.curChar == '\\' or self.curChar == '\t':
                    self.abort("Illegal character in string")
                self.nextChar()
            tok = Token(self.source[startPos:self.curPos], TokenType.STRING)

        elif self.curChar.isdigit():
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.':
                self.nextChar()

                if not self.peek().isdigit():
                    self.abort("Illeagl character in number")
                while self.peek().isdigit():
                    self.nextChar()

            tok = Token(self.source[startPos : self.curPos + 1], TokenType.NUMBER)
        
        elif self.curChar.isalpha():
            startPos = self.curPos
            while self.peek().isalnum():
                self.nextChar()
            
            tokText = self.source[startPos : self.curPos + 1]

            keyword = Token.checkIfKeyword(tokText)
            if keyword == None:
                tok = Token(tokText, TokenType.IDENT)
            else:
                tok = Token(tokText, keyword)

        else:
            self.abort("unknown token" + self.curChar)


        self.nextChar()
        return tok
