import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    q = deque()
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    l = int(input())
    cur = list(map(int, input().split()))
    target = list(map(int, input().split()))

    graph = [[0] * l for _ in range(l)]
    visited = list(graph)

    q.append(cur)
    visited[cur[0]][cur[1]] = 1

    while q:
        x, y = q.popleft()

        if x == target[0] and y == target[1]:
            print(visited[x][y] - 1)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if not 0 <= nx < l:
                continue
            if not 0 <= ny < l:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    