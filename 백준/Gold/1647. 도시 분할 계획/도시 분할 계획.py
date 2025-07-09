
import sys
def sol():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    parent = list(range(n + 1))
    rank = [0] * (n + 1)


    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]

        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root


    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return False

        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True


    graph = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2], reverse=True)
    summed = cnt = highest = 0

    while cnt < n - 1:
        a, b, c = graph.pop()
        if union(a, b):
            summed += c
            cnt += 1
            highest = c

    print(summed - highest)
sol()