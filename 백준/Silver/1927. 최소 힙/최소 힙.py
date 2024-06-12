import heapq
import sys

input=sys.stdin.readline
seq= []

for _ in range(int(input())):
    s=input()
    if s=="0\n":
        print(heapq.heappop(seq) if seq else 0)
    else:
        heapq.heappush(seq, int(s))