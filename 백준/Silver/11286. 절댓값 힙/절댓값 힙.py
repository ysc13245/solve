import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

heap = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(str(heapq.heappop(heap)[1])+"\n" if heap else "0\n")
    else:
        heapq.heappush(heap, (abs(n), n))
