s, e = map(int, input().split())
arr = [1] * (e - s + 1)

for i in range(2, int(pow(e, 0.5)) + 1):
    n = j = i * i
    start = ((s + n - 1) // n) * n
    for j in range(start, e + 1, n):
        arr[j - s] = 0

print(sum(arr))
