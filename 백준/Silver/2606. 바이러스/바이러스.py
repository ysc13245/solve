N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


stack = [1]
visited = set()
trail = []

while stack:
    cur = stack.pop()
    if cur not in visited:
        trail.append(cur)
    visited.add(cur)

    for nxt in graph[cur]:
        if nxt not in visited:
            stack.append(nxt)
print(len(trail)-1)