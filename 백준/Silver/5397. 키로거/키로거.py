import sys

input = sys.stdin.readline
for _ in range(int(input())):
    l, r = [], []
    s = input().rstrip()
    for c in s:
        if c == "<":
            if l:
                r.append(l.pop())
        elif c == ">":
            if r:
                l.append(r.pop())
        elif c == "-":
            if l:
                l.pop()
        else:
            l.append(c)
    print("".join(l + r[::-1]))
