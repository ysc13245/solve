def find(x):
    while parent[x] != x:
        x, parent[x] = parent[x], parent[parent[x]]
    return x


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


import sys

input = sys.stdin.readline
n, m = map(int, input().split())
t, *truth = map(int, input().split())

parent = list(range(n + 1))
rank = [0] * (n + 1)

for i in range(t):
    union(truth[0], truth[i])

party = []

for _ in range(m):
    _, *arr = map(int, input().split())

    for a, b in zip(arr, arr[1:]):
        union(a, b)
    party.append(arr)

cnt = 0

for p in party:
    if t == 0:
        cnt += 1
        continue

    truth_root = find(truth[0])
    if all(find(person) != truth_root for person in p):
        cnt += 1

print(cnt)