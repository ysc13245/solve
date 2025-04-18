from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([(0, 0)])
visited = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]
visited[0][0] = True
dist[0][0] = 1

while queue:
    x, y = queue.popleft()
    if x == n - 1 and y == m - 1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == "0":
            continue
        if visited[nx][ny]:
            continue

        queue.append((nx, ny))
        visited[nx][ny] = True
        dist[nx][ny] = dist[x][y] + 1

print(dist[n - 1][m - 1])
