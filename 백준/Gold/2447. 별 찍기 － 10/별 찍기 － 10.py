def draw(sr, sc, grid, size):
    if size == 3:
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    continue
                grid[sr + i][sc + j] = "*"
        return

    size = size // 3
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            draw(sr + i * size, sc + j * size, grid, size)


n = int(input())
grid = [[" "] * n for _ in range(n)]
draw(0, 0, grid, n)
print("\n".join("".join(row) for row in grid))