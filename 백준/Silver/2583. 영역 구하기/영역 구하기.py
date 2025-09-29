import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
canvas = [[0] * (m) for _ in range(n)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            canvas[y][x] = 1

for i in range(n):
    for j in range(m):

        if canvas[i][j]:
            continue

        cnt = 1
        canvas[i][j] = 1
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if canvas[nx][ny]:
                        continue

                    canvas[nx][ny] = 1
                    stack.append((nx, ny))
                    cnt += 1
        ans.append(cnt)
ans.sort()

print(len(ans))
print(*ans)
