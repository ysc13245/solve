import sys

input = sys.stdin.readline
n = int(input())
arr = [input().strip() for _ in range(n)]
arr.sort()
cnt = 0

for i, v in enumerate(arr[:-1]):
    if arr[i + 1].startswith(v):
        cnt += 1

print(n - cnt)
