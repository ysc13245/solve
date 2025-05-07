import sys

input = sys.stdin.readline
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0] * n for _ in range(n)]
cnt = [0, 0]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue

        cnt[0] += 1
        stack = [(i, j)]
        visited[i][j] = 1
        cur = graph[i][j]
        while stack:
            x, y = stack.pop()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                if not 0 <= nx < n:
                    continue
                if not 0 <= ny < n:
                    continue
                if visited[nx][ny]:
                    continue

                nxt = graph[nx][ny]
                if nxt == cur:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))


visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue

        cnt[1] += 1
        stack = [(i, j)]
        visited[i][j] = 1
        cur = graph[i][j]
        while stack:
            x, y = stack.pop()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                if not 0 <= nx < n:
                    continue
                if not 0 <= ny < n:
                    continue
                if visited[nx][ny]:
                    continue

                nxt = graph[nx][ny]
                if cur == "B":
                    if nxt == "B":
                        visited[nx][ny] = 1
                        stack.append((nx, ny))
                else:
                    if nxt != "B":
                        visited[nx][ny] = 1
                        stack.append((nx, ny))

print(cnt[0], cnt[1])
