def sol():
    import sys
    input = sys.stdin.readline
    print = sys.stdout.write

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x


    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return
        elif root_x < root_y:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x


    n, m = map(int, input().split())
    parent = list(range(n + 1))

    for _ in range(m):
        o, a, b = map(int, input().split())
        if o == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print("YES\n")
            else:
                print("NO\n")

sol()