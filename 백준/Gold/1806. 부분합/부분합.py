n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = right = summed = 0
minimum = float("inf")

while True:
    if summed >= s:
        minimum = min(minimum, right - left)
        summed -= arr[left]
        left += 1
    else:
        if right >= n:
            break

        summed += arr[right]
        right += 1

print(minimum if minimum != float("inf") else 0)
