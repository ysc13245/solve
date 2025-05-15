def sol():
    from collections import deque
    import sys

    input = sys.stdin.readline

    m, n, h = map(int, input().split())
    tomatos = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

    q = deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomatos[i][j][k] == 1:
                    q.append((i, j, k))

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h:
                continue
            if ny < 0 or ny >= n:
                continue
            if nz < 0 or nz >= m:
                continue

            if tomatos[nx][ny][nz] == 0:
                tomatos[nx][ny][nz] = tomatos[x][y][z] + 1
                q.append((nx, ny, nz))

    result = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomatos[i][j][k] == 0:
                    print(-1)
                    return
                result = max(result, tomatos[i][j][k])

    print(result - 1)
    return


sol()
