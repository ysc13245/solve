import sys


n, m = map(int, input().split())

stack = [[[], 0]]
result = []

while stack:
    current, depth = stack.pop()

    if depth == m:
        print(" ".join(map(str, current)))
        continue

    start = current[-1] if current else 1
    for i in range(n, start - 1, -1):
        stack.append((current + [i], depth + 1))
