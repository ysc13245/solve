import sys

input = sys.stdin.readline


def solve():
    r, c, t = map(int, input().split())
    graph = []
    purifier = []

    for i in range(r):
        row = list(map(int, input().split()))
        if row[0] == -1:
            purifier.append(i)
        graph.append(row)

    def spread():
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        buffer = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if graph[i][j] > 0:
                    spread_amount = graph[i][j] // 5
                    spread_count = 0

                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if not (0 <= ni < r and 0 <= nj < c) or graph[ni][nj] == -1:
                            continue

                        buffer[ni][nj] += spread_amount
                        spread_count += 1

                    graph[i][j] -= spread_amount * spread_count

        for i in range(r):
            for j in range(c):
                graph[i][j] += buffer[i][j]

    def circulate():
        p1, p2 = purifier

        for i in range(p1 - 1, 0, -1):
            graph[i][0] = graph[i - 1][0]
        for j in range(c - 1):
            graph[0][j] = graph[0][j + 1]
        for i in range(p1):
            graph[i][c - 1] = graph[i + 1][c - 1]
        for j in range(c - 1, 1, -1):
            graph[p1][j] = graph[p1][j - 1]
        graph[p1][1] = 0

        for i in range(p2 + 1, r - 1):
            graph[i][0] = graph[i + 1][0]
        for j in range(c - 1):
            graph[r - 1][j] = graph[r - 1][j + 1]
        for i in range(r - 1, p2, -1):
            graph[i][c - 1] = graph[i - 1][c - 1]
        for j in range(c - 1, 1, -1):
            graph[p2][j] = graph[p2][j - 1]
        graph[p2][1] = 0

    for _ in range(t):
        spread()
        circulate()

    res = sum(sum(row) for row in graph) + 2
    print(res)


solve()
