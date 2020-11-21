import sys
import antlr4

from grammar import MySQLLexer
#from grammar import MySQLParser
from grammar import MySQLLexer


LEXER_VALID_STATEMENTS = [
    'select 1 from foo',

    ('\n'
     'select p.id,\n'
     '  p.name,\n'
     '  c.desc ContactDesc,\n'
     '  a.desc AddressDesc\n'
     'from profile p\n'
     'inner join contact c\n'
     '  on p.id = c.profileid\n'
     'inner join address a\n'
     '  on p.id = a.profileid\n'
     'where p.name = \'bla\'\n'
     '  and c.ord = 1\n'
     '  and a.ord = 1\n'),
]


def test_lexer():
    for stmt in LEXER_VALID_STATEMENTS:
        print(f"\n============\nStatement: {stmt}\n")
        for tok in MySQLLexer(antlr4.InputStream(stmt)).getAllTokens():
            print(f'{tok.text}\t: {MySQLLexer.symbolicNames[tok.type]}')


if __name__ == '__main__':
    test_lexer()
