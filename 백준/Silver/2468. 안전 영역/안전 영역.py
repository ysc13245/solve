import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
res = 0

for t in range(101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > t:
                cnt += 1
                stack = [(i, j)]
                visited[i][j] = True

                while stack:
                    x, y = stack.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny] and arr[nx][ny] > t:
                                stack.append((nx, ny))
                                visited[nx][ny] = True

    res = max(res, cnt)

print(res)
