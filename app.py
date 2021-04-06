"""
Main Calculator Application
Takes two command line arguments:
-s <expression> a single text string that represents an algorithmic expression
-f <filename> a text file with a list of expressions, one per line
"""
import argparse
from calculator import Calculator

def process_expression(expression):
    """
    Simple case - take a single text string representing an algorithmic expression and return the result
    """
    c = Calculator()
    return c.calculate(expression)

def process_file(filename):
    """
    Filename case - take a text file and return an array of results
    """
    c = Calculator()
    results = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            results.append(c.calculate(line))
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculator command line arguments')
    parser.add_argument('-s', action='store', dest='expression',
                        help='string expression to calculate')
    parser.add_argument('-f', action='store', dest='filename',
                        help='filename with list of expressions')

    args = parser.parse_args()

    if args.expression:
        print(process_expression(args.expression))
    elif args.filename:
        print(process_file(args.filename))
    else:
        args.print_help()