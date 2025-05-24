def sol():
    import heapq
    import sys

    input = sys.stdin.readline
    n = int(input())
    arr = sorted([tuple(map(int, input().split())) for _ in range(n)])

    rooms = [arr[0][1]]

    for i in range(1, n):
        if not arr[i][0] < rooms[0]:
            heapq.heappop(rooms)

        heapq.heappush(rooms, arr[i][1])
        
    print(len(rooms))

sol()
