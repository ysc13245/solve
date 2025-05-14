def sol():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    canvas = [list(map(int, input().split())) for _ in range(n)]
    clear = [[0] * m for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    while True:
        if canvas[r][c] == 0 and clear[r][c] == 0:
            clear[r][c] = 1
            cnt += 1

        if all(
            not is_valid(r + nx, c + ny)
            or canvas[r + nx][c + ny]
            or clear[r + nx][c + ny]
            for nx, ny in zip(dx, dy)
        ):
            nx, ny = -dx[d], -dy[d]

            if not is_valid(r + nx, c + ny) or canvas[r + nx][c + ny] == 1:
                break

            r, c = r + nx, c + ny
            continue

        d = (d + 3) % 4

        nx, ny = dx[d], dy[d]
        if (
            is_valid(r + nx, c + ny)
            and canvas[r + nx][c + ny] == 0
            and clear[r + nx][c + ny] == 0
        ):
            r, c = r + nx, c + ny

    print(cnt)


sol()
