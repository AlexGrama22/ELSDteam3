from antlr4 import *
from geometrydslLexer import geometrydslLexer
from geometrydslParser import geometrydslParser
import interpreter
import sys

def main():
    input_stream = FileStream("file.txt")

    lexer = geometrydslLexer(input_stream)

    stream = CommonTokenStream(lexer)
    parser = geometrydslParser(stream)
    tree = parser.start()
    # print(tree.getChildCount())
    # print(tree.toStringTree())
    # print(tree.toStringTree(recog=parser))
    i = interpreter.GInter(tree)
    try:
        i.getVars()
        i.getMeth()

        original_stdout = sys.stdout
        # print(i.vars)
        with open('outputfile.txt', 'w') as file:
            sys.stdout = file
            i.getMeth()
        sys.stdout = original_stdout
    except:
        original_stdout = sys.stdout
        # print(i.vars)
        with open('outputfile.txt', 'w') as file:
            sys.stdout = file
            print('Error')
        sys.stdout = original_stdout
if __name__ == '__main__':
    main()
