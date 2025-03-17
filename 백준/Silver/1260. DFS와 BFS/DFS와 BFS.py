from collections import deque


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph = [sorted(li) for li in graph]


def dfs():
    stack = [v]
    visited = set()
    tail = []

    while stack:
        x = stack.pop()
        if x not in visited:
            tail.append(x)
            visited.add(x)
            next = reversed(graph[x])
            for num in next:
                if num not in visited:
                    stack.append(num)

    print(*tail)


def bfs():
    q = deque([v])
    visited = set()
    tail = []

    while q:
        x = q.popleft()
        if x not in visited:
            tail.append(x)
            visited.add(x)
            q.extend(graph[x])
    print(*tail)


dfs()
bfs()