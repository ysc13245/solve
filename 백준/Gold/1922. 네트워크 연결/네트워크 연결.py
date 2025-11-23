def find(x):
    root = x

    while root != parent[root]:
        root = parent[root]

    while x != root:
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


import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

total, cnt = 0, 0

for a, b, c in graph:
    if union(a, b):
        total += c
        cnt += 1

    if cnt == n - 1:
        break

print(total)
