from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    durations = [0] + list(map(int, input().split()))
    indegree = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())
    dp = [0] * (n + 1)
    q = deque()

    for i in range(1, n + 1):

        if indegree[i]:
            continue

        q.append(i)
        dp[i] = durations[i]

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            dp[next] = max(dp[next], dp[cur] + durations[next])
            indegree[next] -= 1

            if indegree[next] == 0:
                q.append(next)

    print(dp[w])
