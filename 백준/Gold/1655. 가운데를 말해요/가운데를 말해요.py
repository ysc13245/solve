import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
left, right = [], []

for _ in range(n):
    m = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -m)
    else:
        heapq.heappush(right, m)

    if right and -left[0] > right[0]:
        l = heapq.heappop(left)
        r = heapq.heappop(right)
        heapq.heappush(left, -r)
        heapq.heappush(right, -l)

    print(str(-left[0]) + '\n')