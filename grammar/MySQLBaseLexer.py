from antlr4 import Lexer


class MySQLBaseLexer(Lexer):
    def determineNumericType(self, s: str):
        pass

    def setType(self, *a, **kw):
        pass
    
    def getText(self, *a, **kw):
        pass

    def emitDot(self, *a, **kw):
        pass

    def isSqlModeActive(self, *a, **kw):
        pass

    NoBackslashEscapes = True



