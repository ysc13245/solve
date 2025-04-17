import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lis = list(map(int, (input() for _ in range(n))))

start, end = 1, max(lis)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in lis:
        cnt += l // mid

    if cnt >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)
