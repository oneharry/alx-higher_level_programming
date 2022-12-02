#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    av = sys.argv
    le = len(av)
    if le - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(av[0]))
        sys.exit(1)
    else:
        opera = "+-*/"
        if av[2] not in opera:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(av[1])
            b = int(av[3])
            result = 0
            if av[2] == "+":
                result = add(a, b)
            elif av[2] == "-":
                result = sub(a, b)
            elif av[2] == "*":
                result = mul(a, b)
            elif av[2] == "/":
                result = div(a, b)
            print("{} {} {} = {}".format(a, av[2], b, result))
