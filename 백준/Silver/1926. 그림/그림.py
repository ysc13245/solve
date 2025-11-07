n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
sizes = []
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            stack = [(i, j)]
            visited[i][j] = True
            size = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < n
                        and 0 <= ny < m
                        and graph[nx][ny]
                        and not visited[nx][ny]
                    ):
                        stack.append((nx, ny))
                        visited[nx][ny] = True
                        size += 1
            sizes.append(size)
print(len(sizes))
print(max(sizes) if sizes else 0)
