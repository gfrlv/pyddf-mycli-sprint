from antlr4 import Lexer


class MySQLBaseLexer(Lexer):
    def __init__(self, server_version, *a, **kw):
        self.server_version = server_version
        super().__init__(*a, **kw)
        self.pending_tokens = []

    def determineNumericType(self, s: str):
        pass
    #     LENGTH_LONG = 10
    #     LENGTH_LONGLONG = 19
    #     LENGTH_SIGNED_LONGLONG = 19
    #     LENGTH_UNSIGNED_LONGLONG = 20
    #
    #     value = int(s)
    #     s_normalized = str(value) if value >= 0 else str(value)[1:]
    #
    #     length = len(s_normalized)
    #     if length < LENGTH_LONG:
    #         return self.INT_NUMBER
    #
    #     if value < 0


    def setType(self, *a, **kw):
        pass
    
    def getText(self, *a, **kw):
        print('getText')
        pass

    def emitDot(self, *a, **kw):
        t = self._factory.create(self._tokenFactorySourcePair, self.DOT_SYMBOL, self._text, self._channel,
                                 self._tokenStartCharIndex,
                                 self._tokenStartCharIndex, self._tokenStartLine, self._tokenStartColumn)
        self.pending_tokens.append(t)
        self._tokenStartCharIndex += 1

    def isSqlModeActive(self, *a, **kw):
        pass

    def nextToken(self):
        if self.pending_tokens:
            return self.pending_tokens.pop()

        next_token = super().nextToken()
        if self.pending_tokens:
            pending_token = self.pending_tokens.pop()
            self.pending_tokens.append(next_token)
            return pending_token

        return next_token

    def checkVersion(self, s: str):
        pass

    def determineFunction(self, token: int):
        return

    NoBackslashEscapes = True
    inVersionComment = True
    PipesAsConcat = True
