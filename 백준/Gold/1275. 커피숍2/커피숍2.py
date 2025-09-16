import sys


def update(i, v):
    while i <= n:
        tree[i] += v
        i += i & -i


def prefix_sum(i):
    summed = 0
    while i > 0:
        summed += tree[i]
        i -= i & -i
    return summed


def range_sum(start, end):
    return prefix_sum(max(start, end)) - prefix_sum(min(start, end) - 1)


input = sys.stdin.readline
print = sys.stdout.write
n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
tree = [0] * (n + 1)

for i in range(1, n + 1):
    update(i, arr[i])

for _ in range(q):
    x, y, a, b = map(int, input().split())

    print(str(range_sum(x, y)) + "\n")
    diff = b - arr[a]
    update(a, diff)
    arr[a] = b