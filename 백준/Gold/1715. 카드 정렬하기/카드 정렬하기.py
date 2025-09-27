import sys
from heapq import *

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
heapify(arr)
ans = 0

while len(arr) > 1:
    n1 = heappop(arr)
    n2 = heappop(arr)
    ans += n1 + n2
    heappush(arr, n1 + n2)

print(ans)
