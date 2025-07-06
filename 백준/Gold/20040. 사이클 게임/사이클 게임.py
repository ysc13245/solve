import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


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
        parent[root_y] = root_x
        rank[root_x] += 1
    return True


input = sys.stdin.readline
n, m = map(int, input().split())
parent = list(range(n))
rank = [0] * (n)

for i in range(m):
    a, b = map(int, input().split())
    if not union(a, b):
        print(i + 1)
        break
else:
    print(0)
