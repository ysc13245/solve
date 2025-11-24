from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())

board = []
start = None

for i in range(n):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v == 2:
            start = (i, j)
    board.append(row)

dist = [[-1] * m for _ in range(n)]

q = deque()
sx, sy = start
q.append((sx, sy))
dist[sx][sy] = 0

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print("0 ")
        else:
            print(str(dist[i][j]) + " ")
    print("\n")
