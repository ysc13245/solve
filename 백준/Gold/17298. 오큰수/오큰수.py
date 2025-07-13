import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n
stack = []

for i, v in enumerate(arr):
    while stack and arr[stack[-1]] < v:
        ans[stack.pop()] = v
    stack.append(i)

print(*ans)
