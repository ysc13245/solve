import sys

input =sys.stdin.readline

N, K = map(int, input().split())
ice = [0] * 1000001
l = 0
for _ in range(N):
    a, b = map(int, input().split())
    ice[b] = a
    l = max(l, b)
ice = ice[: l + 1]

m = 0
i = 0
sum = sum(ice[: K * 2 + 1])
while True:
    try:
        m = max(m, sum)
        sum += ice[i + K * 2 + 1]
        sum -= ice[i]
        i += 1
    except:
        m = max(m, sum)
        break
print(m)
