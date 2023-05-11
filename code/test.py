import sys

import FileStream as FileStream
from antlr4 import *
from geometrydslLexer import geometrydslLexer
from geometrydslParser import geometrydslParser


def main(argv):
    input_stream = FileStream(argv[1])

    lexer = geometrydslLexer(input_stream)


    stream = CommonTokenStream(lexer)
    parser = geometrydslParser(stream)
    tree = parser.start()

    print(tree.toStringTree())
    print(tree.toStringTree(recog=parser))

 
if __name__ == '__main__':
    main(sys.argv)
