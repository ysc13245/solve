import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

dp = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    dp[a-1][b-1] = 1
    dp[b-1][a-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

print(min(range(n), key=lambda i: sum(dp[i])) + 1)