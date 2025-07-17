import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = []

for i in range(5):
    for j in range(i + 1, 5):
        res.append((sum(row[i] and row[j] for row in arr), (i, j)))
best = max(res, key=lambda x: x[0])
ans = [0] * 5
for i in best[1]:
    ans[i] = 1
print(best[0])
print(*ans)