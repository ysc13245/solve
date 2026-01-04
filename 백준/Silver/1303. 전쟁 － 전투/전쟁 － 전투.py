import sys

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = [0, 0]

for i in range(m):
    for j in range(n):
        if visited[i][j]:
            continue

        cnt = 0
        stack = [(i, j)]

        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue

            visited[x][y] = True
            cnt += 1

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                if board[nx][ny] != board[i][j]:
                    continue
                stack.append((nx, ny))

        res[int(board[i][j] == "B")] += cnt**2

print(*res)
