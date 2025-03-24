from collections import defaultdict
from functools import reduce
import sys

input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print("0\n")
        continue
    
    data = defaultdict(set)
    for _ in range(n):
        s = input().split()
        data[s[1]].add(s[0])

    print(
        str(reduce(lambda x, y: x * y, (len(v) + 1 for v in data.values())) - 1) + "\n"
    )
