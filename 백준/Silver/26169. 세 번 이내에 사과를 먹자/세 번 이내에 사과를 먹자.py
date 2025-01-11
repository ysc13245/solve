graph = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
stack = [[(r, c), 0, 0, set()]]

while stack:
    (r, c), turn, apple, visited = stack.pop()
    visited.add((r, c))
    if graph[r][c] == 1:
        apple += 1

    if apple >= 2:
        print(1)
        break
    if turn >= 3:
        continue

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if (
            0 <= nr < 5
            and 0 <= nc < 5
            and graph[nr][nc] != -1
            and (nr, nc) not in visited
        ):
            stack.append([(nr, nc), turn + 1, apple, set(visited)])
else:
    print(0)
