import sys


def sol():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    grid = [input().strip() for _ in range(r)]
    grid_idx = [[ord(ch) - 65 for ch in row] for row in grid]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [0] * 26
    visited[grid_idx[0][0]] = 1

    stack = [[0, 0, 1, 0]]
    ans = 1

    while stack:
        x, y, cnt, d = stack[-1]
        if d == 4:
            stack.pop()
            visited[grid_idx[x][y]] = 0
            continue

        stack[-1][3] += 1

        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < r and 0 <= ny < c:
            idx = grid_idx[nx][ny]
            if visited[idx] == 0:
                visited[idx] = 1
                stack.append([nx, ny, cnt + 1, 0])
                if cnt + 1 > ans:
                    ans = cnt + 1

    print(ans)


sol()
