import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
graph = [list(input().rstrip()) for _ in range(n)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

q = deque([(0, 0, 0)])
visited[0][0][0] = 1

while q:
    x, y, b = q.popleft()

    if x == n - 1 and y == m - 1:
        print(visited[x][y][b])
        break

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:

            if visited[nx][ny][b]:
                continue

            if graph[nx][ny] == "1" and b == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))

            elif graph[nx][ny] == "0" and visited[nx][ny][b] == 0:
                visited[nx][ny][b] = visited[x][y][b] + 1
                q.append((nx, ny, b))

else:
    print(-1)
