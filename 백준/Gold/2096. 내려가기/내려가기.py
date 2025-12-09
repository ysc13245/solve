import sys

input = sys.stdin.readline
n = int(input())
min1, min2, min3 = map(int, input().split())
max1, max2, max3 = min1, min2, min3

for _ in range(1, n):
    a, b, c = map(int, input().split())

    new_min1 = min(min1, min2) + a
    new_min2 = min(min1, min2, min3) + b
    new_min3 = min(min2, min3) + c

    new_max1 = max(max1, max2) + a
    new_max2 = max(max1, max2, max3) + b
    new_max3 = max(max2, max3) + c

    min1, min2, min3 = new_min1, new_min2, new_min3
    max1, max2, max3 = new_max1, new_max2, new_max3

print(max(max1, max2, max3), min(min1, min2, min3))