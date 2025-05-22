s = input()
stack = 0
cnt = 0

for i, c in enumerate(s):
    if c == "(":
        stack += 1
    else:
        stack -= 1
        if s[i - 1] == "(":
            cnt += stack

        else:
            cnt += 1
print(cnt)
