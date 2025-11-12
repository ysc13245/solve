import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, [input() for _ in range(n)]))

dp = [float("inf")] * (k + 1)
dp[0] = 0

for e in arr:
    for i in range(e, k + 1):
        dp[i] = min(dp[i], dp[i - e] + 1)

print(dp[k] if dp[k] != float("inf") else -1)
