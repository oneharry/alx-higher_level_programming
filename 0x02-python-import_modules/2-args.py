#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    av = sys.argv
    le = len(av)
    if le == 1:
        print("0 arguments.")
    elif le == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(le - 1))
    for i in range(1, le):
        print("{}: {}".format(i, av[i]))
