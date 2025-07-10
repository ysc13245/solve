def dijkstra(start):
    visited = [False] * (n + 1)
    distance[start] = 0

    for _ in range(n - 1):
        node, min_dist= -1, INF

        for i in range(1, n+1):
            if not visited[i] and min_dist > distance[i]:
                node = i
                min_dist = distance[i]

        visited[node] = True

        if node == end:
            return
        
        for next_node, dist in graph[node]:
            next_dist = distance[node] + dist

            if not visited[next_node] and next_dist < distance[next_node]:
                distance[next_node] = next_dist

import sys

input = sys.stdin.readline
INF = float("inf")
n = int(input())
m = int(input())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])
