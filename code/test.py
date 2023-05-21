from antlr4 import *
from geometrydslLexer import geometrydslLexer
from geometrydslParser import geometrydslParser
import interpreter


def main():
    input_stream = FileStream("file.txt")

    lexer = geometrydslLexer(input_stream)

    stream = CommonTokenStream(lexer)
    parser = geometrydslParser(stream)
    tree = parser.start()
    print(tree.getChildCount())
    print(tree.toStringTree())
    print(tree.toStringTree(recog=parser))
    i = interpreter.GInter(tree)
    i.getVars()
    i.getMeth()
    print(i.vars)


if __name__ == '__main__':
    main()
