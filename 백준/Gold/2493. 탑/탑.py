n = int(input())
arr = list(map(int, input().split()))

stack = []
ans = []

for i, h in enumerate(arr, start=1):
    while stack and stack[-1][1] < h:
        stack.pop()

    if stack:
        ans.append(stack[-1][0])
    else:
        ans.append(0)
    stack.append((i, h))

print(*ans)
