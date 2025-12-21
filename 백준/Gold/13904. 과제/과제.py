import sys

input = sys.stdin.readline
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1], reverse=True)

res = [0]*1001
for d, w in arr:
    for day in range(d, 0, -1):
        if res[day] == 0:
            res[day] = w
            break

print(sum(res))
