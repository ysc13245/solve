def sol():
    import sys
    import heapq

    input = sys.stdin.readline

    n = int(input())
    heap = []

    for _ in range(n):
        m = int(input())
        if m == 0:
            print(-heapq.heappop(heap) if heap else 0)
        else:
            heapq.heappush(heap, -m)
sol()