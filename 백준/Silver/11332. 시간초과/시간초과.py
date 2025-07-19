import math
import sys


def sol():
    input = sys.stdin.readline
    print = sys.stdout.write
    cal = {
        "O(N)": lambda x, y: int(x) * int(y),
        "O(N^2)": lambda x, y: int(x) ** 2 * int(y),
        "O(N^3)": lambda x, y: int(x) ** 3 * int(y),
        "O(2^N)": lambda x, y: 2 ** int(x) * int(y),
        "O(N!)": lambda x, y: math.factorial(int(x)) * int(y),
    }

    for _ in range(int(input())):
        order, *data, t = input().split()
        print("May Pass.\n" if cal[order](*data) <= int(t) * pow(10, 8) else "TLE!\n")


sol()
