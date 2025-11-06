from collections import deque
import sys

input = sys.stdin.readline
v, e = map(int, input().split())

indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
res = []

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    res.append(cur)
    for next in graph[cur]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

print(*res)
