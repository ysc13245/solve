import sys
from heapq import heappop, heappush


def dijkstra(start):
    heap = [(0, start)]
    distance[start] = 0

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distance[node]:
            continue

        for next_node, d in graph[node]:
            next_dist = min_dist + d

            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))


input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
distance = [float("inf")] * (v + 1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start)

print(*(x if x != float("inf") else "INF" for x in distance[1:]), sep="\n")
