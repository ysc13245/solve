n = int(input())
dp = [False] * 10001

dp[1:4] = [1, 0, 1]
for i in range(4, n + 1):
    dp[i] = not (dp[i - 1] or dp[i - 3])
print("SK" if dp[n] else "CY")
