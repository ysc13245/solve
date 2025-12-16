import sys

input = sys.stdin.readline
n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (t + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, t + 1):
        k, s = arr[i - 1]

        dp[i][j] = dp[i - 1][j]

        if k <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - k] + s)

print(dp[n][t])
