import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


cnt = 0
visited = set()

for start in range(1, n + 1):
    if start in visited:
        continue

    cnt += 1
    stack = [start]

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        stack.extend(graph[current])


print(cnt)
