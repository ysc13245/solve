from heapq import heappush, heappop
import sys

input = sys.stdin.readline
heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for num in numbers:
        if len(heap) < n:
            heappush(heap, num)
        else:
            if num > heap[0]:
                heappop(heap)
                heappush(heap, num)

print(heap[0])
