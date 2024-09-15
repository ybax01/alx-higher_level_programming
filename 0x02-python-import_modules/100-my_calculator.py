#!/usr/bin/python3

import sys
from calculator_1.py import add, sub, mul, div

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    ops = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
            }

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    res = ops[op](a, b)
    print("{} {} {}".format(a, b, res))


if __name__ == "__main__":
    main()
