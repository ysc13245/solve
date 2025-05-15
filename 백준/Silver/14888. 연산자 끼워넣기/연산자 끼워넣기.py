import math


n = int(input())
iarr = list(map(int, input().split()))

oper = {symbol: cnt for symbol, cnt in zip("+-*/", map(int, input().split()))}

min_result = math.inf
max_result = -min_result

stack = []
stack = [(1, iarr[0], dict(oper))]

while stack:
    idx, cur, ops = stack.pop()

    if idx == n:
        max_result = max(max_result, cur)
        min_result = min(min_result, cur)
        continue

    num = iarr[idx]
    if ops["+"]:
        new_ops = dict(ops)
        new_ops["+"] -= 1
        stack.append((idx + 1, cur + num, new_ops))

    if ops["-"]:
        new_ops = dict(ops)
        new_ops["-"] -= 1
        stack.append((idx + 1, cur - num, new_ops))

    if ops["*"]:
        new_ops = dict(ops)
        new_ops["*"] -= 1
        stack.append((idx + 1, cur * num, new_ops))

    if ops["/"]:
        new_ops = dict(ops)
        new_ops["/"] -= 1
        stack.append((idx + 1, int(cur / num), new_ops))

print(max_result)
print(min_result)
