import sys

input = sys.stdin.readline

n = int(input())
s, e = sorted(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


stack = [(s, 0)]
visited = set()


while stack:
    v, depth = stack.pop()
    if v in visited:
        continue

    if v == e:
        print(depth)
        break

    visited.add(v)
    for nxt in graph[v]:
        stack.append((nxt, depth + 1))
        
else:
    print(-1)
