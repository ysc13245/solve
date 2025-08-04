n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False] * n
seq = []


def dfs(depth):
    used = set()
    if depth == m:
        print(*seq)
        return

    for i in range(n):
        if visited[i]:
            continue
        if arr[i] in used:
            continue

        visited[i] = True
        used.add(arr[i])
        seq.append(arr[i])

        dfs(depth + 1)

        visited[i] = False
        seq.pop()


dfs(0)
