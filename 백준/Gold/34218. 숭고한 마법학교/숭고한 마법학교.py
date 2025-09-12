import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(n)]
start = tuple(map(lambda x: int(x) - 1, input().split()))
goal = tuple(map(lambda x: int(x) - 1, input().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
start_area = []
goal_area = []
ans = -1
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if canvas[i][j] and not visited[i][j]:
            stack = [(i, j)]
            area = [(i, j)]
            visited[i][j] = True

            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]

                    if not (0 <= nx < n and 0 <= ny < m):
                        continue
                    if visited[nx][ny]:
                        continue
                    if canvas[nx][ny] == 0:
                        continue

                    stack.append((nx, ny))
                    area.append((nx, ny))
                    visited[nx][ny] = True
            if start in area:
                start_area = area
            if goal in area:
                goal_area = area

if not start_area or not goal_area:
    ans = -1

elif start_area == goal_area:
    ans = 0
else:
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    for x, y in start_area:
        dist[x][y] = 0
        q.append((x, y))

    goal_set = set(goal_area)
    found = False
    while q and not found:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if dist[nx][ny] != -1:
                continue

            dist[nx][ny] = dist[x][y] + 1

            if (nx, ny) in goal_set:
                ans = dist[nx][ny]
                found = True
                break

            q.append((nx, ny))

print(ans)
