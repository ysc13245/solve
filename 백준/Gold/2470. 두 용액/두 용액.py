n = int(input())
arr = list(map(int, input().split()))
arr.sort()


l, r = 0, n - 1
ans = (float("inf"), float("inf"))

while l < r:
    summed = arr[l] + arr[r]
    if abs(sum(ans)) > abs(summed):
        ans = (arr[l], arr[r])

    if summed == 0:
        ans = (arr[l], arr[r])
        break

    elif summed < 0:
        l += 1
    else:
        r -= 1

print(*ans)
