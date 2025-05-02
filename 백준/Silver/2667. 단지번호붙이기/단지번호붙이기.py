import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total = 0
cnts = []

for i in range(n):
    for j in range(n):
        if arr[i][j] and visited[i][j] == 0:
            cnt = 1
            total += 1
            visited[i][j] = 1
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if not 0 <= nx < n:
                        continue
                    if not 0 <= ny < n:
                        continue
                    if arr[nx][ny] == 0:
                        continue
                    if visited[nx][ny]:
                        continue

                    visited[nx][ny] = 1
                    cnt += 1
                    stack.append((nx, ny))
            cnts.append(cnt)
print(total)
print(*sorted(cnts), sep="\n")
