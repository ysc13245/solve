def sol():
    import sys

    input = sys.stdin.readline
    print = sys.stdout.write

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
            rank[root_y] += 1
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
            rank[root_x] += 1
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    n = int(input())
    m = int(input())

    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    matrix = [list(map(int, input().split())) for _ in range(n)]

    arr = list(map(int, input().split()))

    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                union(i + 1, j + 1)

    for i in range(m - 1):
        if find(arr[i]) != find(arr[i + 1]):
            print("NO")
            return
            
    print("YES")


sol()
