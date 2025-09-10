n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n):
    if not s:
        break

    t = min(n, s + i + 1)
    idx = i
    for j in range(i + 1, t):
        if arr[j] > arr[idx]:
            idx = j

    for k in range(idx, i, -1):
        arr[k], arr[k - 1] = arr[k - 1], arr[k]
    s -= idx - i

print(*arr)
