import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    
    INF = float('inf')
    dp = [INF] * (n + 1)
    dp[0] = 0
    if n >= 2:
        dp[2] = 1
    if n >= 4:
        dp[4] = 2
    if n >= 5:
        dp[5] = 1
    
    for i in range(6, n + 1):
        dp[i] = min(dp[i - 2], dp[i - 5]) + 1
    
    print(dp[n] if dp[n] != INF else -1)


solve()