n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)
while start <= end:
    mid = (start + end) // 2
    total = sum(max(tree - mid, 0) for tree in trees)

    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)