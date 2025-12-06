import sys, heapq

input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    n = int(input())
    min_heap = []
    max_heap = []
    cnt = {}

    for _ in range(n):
        op, x = input().split()
        x = int(x)

        if op == "I":
            heapq.heappush(min_heap, x)
            heapq.heappush(max_heap, -x)
            cnt[x] = cnt.get(x, 0) + 1
        else:
            if x == 1:
                while max_heap and cnt[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    cnt[-max_heap[0]] -= 1
            elif x == -1:
                while min_heap and cnt[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    cnt[min_heap[0]] -= 1

    while max_heap and cnt[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and cnt[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(str(-max_heap[0]) + " " + str(min_heap[0]) + "\n")
    else:
        print("EMPTY\n")
