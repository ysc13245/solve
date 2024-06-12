import heapq
import sys

input=sys.stdin.readline
print = sys.stdout.write

seq= []
for _ in range(int(input())):
    s=input()
    if s=="0\n":
        print(str(heapq.heappop(seq))+"\n" if seq else "0\n")
    else:
        heapq.heappush(seq, int(s))