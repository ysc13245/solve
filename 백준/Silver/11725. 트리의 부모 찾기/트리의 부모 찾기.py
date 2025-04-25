import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
parent = [0] * (n + 1)


for _ in range(n - 1):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

stack = [1]
visited[1] = 1

while stack:
    cur = stack.pop()
    visited[cur] = 1
    for v in graph[cur]:
        if visited[v]:
            continue

        stack.append(v)
        visited[v] = 1
        parent[v] = cur

print("\n".join(map(str, parent[2:])))
