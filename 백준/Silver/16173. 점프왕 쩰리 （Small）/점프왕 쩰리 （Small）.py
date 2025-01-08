N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
stack = []
v=graph[0][0]
cur = [0, 0]
if cur[0] + v < N:
    stack.append((cur[0] + v, cur[1]))

if cur[1] + v < N:
    stack.append((cur[0], cur[1] + v))

visited = [[0] * N for _ in range(N)]

while stack:
    x, y = stack.pop()
    if visited[x][y]:
        continue

    visited[x][y] = 1
    if x == N - 1 and y == N - 1:
        print("HaruHaru")
        break

    v = graph[x][y]
    if x + v < N:
        stack.append((x + v, y))
    if y + v < N:
        stack.append((x, y + v))


else:
    print("Hing")