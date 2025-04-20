from collections import deque
import sys

input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    canvas = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            if canvas[i][j] == 0:
                continue
            cnt += 1

            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for d in range(8):
                    nx, ny = x + dx[d], y + dy[d]
                    if not 0 <= nx < n:
                        continue
                    if not 0 <= ny < m:
                        continue
                    if visited[nx][ny]:
                        continue
                    if canvas[nx][ny] == 0:
                        continue

                    visited[nx][ny] = True
                    q.append((nx, ny))
    print(cnt)
