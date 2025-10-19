from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    n, l, r = map(int, input().split())
    canvas = [list(map(int, input().split())) for _ in range(n)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    t = 0

    while True:
        visited = [[False] * n for _ in range(n)]
        move = False

        for i in range(n):
            for j in range(n):

                if visited[i][j]:
                    continue

                q = deque([(i, j)])
                visited[i][j] = True
                group = [(i, j)]
                summed = canvas[i][j]

                while q:
                    x, y = q.popleft()

                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if l <= abs(canvas[x][y] - canvas[nx][ny]) <= r:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                group.append((nx, ny))
                                summed += canvas[nx][ny]

                if len(group) > 1:
                    move = True
                    avg = summed // len(group)
                    for x, y in group:
                        canvas[x][y] = avg

        if not move:
            break

        t += 1

    print(t)


solution()
