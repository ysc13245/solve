def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]

    while x != parent[x]:
        parent[x], x = root, parent[x]

    return root


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return False

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
        rank[root_x] += 1
    return True


import sys

input = sys.stdin.readline

v, e = map(int, input().split())
graph = sorted([list(map(int, input().split())) for _ in range(e)], key=lambda x: x[2])
sum = 0

parent = list(range(v + 1))
rank = [0] * (v + 1)

for a, b, c in graph:
    if union(a, b):
        sum += c
print(sum)
