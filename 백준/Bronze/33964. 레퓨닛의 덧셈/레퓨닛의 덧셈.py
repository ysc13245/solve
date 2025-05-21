n, m = map(int, input().split(" "))
ans = 0
for i in range(n):
    ans += 10**i
for i in range(m):
    ans += 10**i

print(ans)
