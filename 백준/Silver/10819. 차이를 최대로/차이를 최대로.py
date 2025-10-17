n = int(input())
arr = list(map(int, input().split()))
ans = 0

stack = [([], 0)]

while stack:
    nums, depth = stack.pop()

    if depth == n:
        summed = 0

        for i in range(n - 1):
            summed += abs(arr[nums[i]] - arr[nums[i + 1]])

        ans = max(ans, summed)
        continue

    for i in range(n):
        if i in nums:
            continue

        stack.append((nums + [i], depth + 1))

print(ans)
