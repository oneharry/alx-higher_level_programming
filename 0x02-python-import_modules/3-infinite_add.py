#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    av = sys.argv
    le = len(av)
    total = 0
    for i in range(1, le):
        total += int(av[i])
    print(total)
