import sys

input = sys.stdin.readline
for i in range(int(input())):

    m, n, k = map(int, input().split(" "))

    field = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split(" "))
        field[y][x] = 1

    cnt = 0
    visited = []

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and (i, j) not in visited:
                cnt += 1
                visited.append((i, j))
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if (
                        x - 1 >= 0
                        and field[x - 1][y] == 1
                        and (x - 1, y) not in visited
                    ):
                        visited.append((x - 1, y))
                        stack.append((x - 1, y))
                    if x + 1 < n and field[x + 1][y] == 1 and (x + 1, y) not in visited:
                        visited.append((x + 1, y))
                        stack.append((x + 1, y))
                    if (
                        y - 1 >= 0
                        and field[x][y - 1] == 1
                        and (x, y - 1) not in visited
                    ):
                        visited.append((x, y - 1))
                        stack.append((x, y - 1))
                    if y + 1 < m and field[x][y + 1] == 1 and (x, y + 1) not in visited:
                        visited.append((x, y + 1))
                        stack.append((x, y + 1))

    print(cnt)
