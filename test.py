import sys
import antlr4

from grammar import MySQLLexer
from grammar import MySQLParser
from grammar import MySQLLexer


LEXER_VALID_STATEMENTS = [
    'select 1 from foo'
]

def test_lexer():
    for stmt in LEXER_VALID_STATEMENTS:
        for tok in  MySQLLexer(antlr4.InputStream(stmt)).getAllTokens():
            print(tok.text)

