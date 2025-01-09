M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = set()
stack = [(0, 0)]
while stack:
    cur = stack.pop()
    visited.add((cur[0], cur[1]))

    if cur == ((N - 1), M - 1):
        print("Yes")
        break

    if cur[0] + 1 < N:
        if (cur[0] + 1, cur[1]) not in visited and graph[cur[0] + 1][cur[1]]:
            stack.append((cur[0] + 1, cur[1]))

    if cur[1] + 1 < M:
        if (cur[0], cur[1] + 1) not in visited and graph[cur[0]][cur[1] + 1]:
            stack.append((cur[0], cur[1] + 1))

else:
    print("No")
