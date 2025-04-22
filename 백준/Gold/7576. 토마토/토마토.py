from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            q.append((i, j))
while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not 0 <= nx < m:
            continue
        if not 0 <= ny < n:
            continue
        if arr[nx][ny] == 0:
            q.append((nx, ny))
            arr[nx][ny] = arr[x][y] + 1
            ans = arr[nx][ny]

for sub in arr:
    if 0 in sub:
        print(-1)
        break
else:
    print(ans - 1 if ans else 0)