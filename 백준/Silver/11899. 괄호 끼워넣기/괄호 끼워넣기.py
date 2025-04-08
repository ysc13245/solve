stack = []
cnt = 0
for c in input():
    try:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                cnt += 1
    except:
        cnt += 1
print(cnt + len(stack))
