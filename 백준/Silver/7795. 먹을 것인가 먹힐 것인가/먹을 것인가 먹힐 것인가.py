t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 0

    for size in a:
        s, e = 0, m - 1
        while s <= e:
            mid = (s + e) // 2
            if b[mid] >= size:
                e = mid - 1
            else:
                s = mid + 1
        ans += s

    print(ans)
