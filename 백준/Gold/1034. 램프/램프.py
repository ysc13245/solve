import sys
from collections import Counter

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
k = int(input())

counter = Counter(arr)
ans = 0

for row, row_cnt in counter.items():
    zero = row.count("0")

    if zero > k:
        continue
    if zero % 2 != k % 2:
        continue

    ans = max(ans, row_cnt)

print(ans)
