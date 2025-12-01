def check(m, size):
    cnt, cur = 1, 0

    for el in arr:
        if cur + el > size:
            cnt += 1
            cur = el
            if cnt > m:
                return False
        else:
            cur += el

    return True


n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = max(arr)
right = sum(arr)
ans = right

while left <= right:
    mid = (left + right) // 2
    if check(m, mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)