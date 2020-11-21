# pyddf-mycli-sprint

Setting up antlr:

```
wget http://www.antlr.org/download/antlr-4.7.2-complete.jar > bin
export CLASSPATH=${PWD}"/antlr-4.7.2-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java org.antlr.v4.gui.TestRig'
```

Generating the parser:
```
cd grammars
antlr4 -Dlanguage=Python3 MySQLLexer.g4  MySQLParser.g4
```
