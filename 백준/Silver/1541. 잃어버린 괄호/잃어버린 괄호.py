expression = input().split("-")

for i, v in enumerate(expression):
    if "+" in v:
        expression[i] = sum(map(int, v.split("+")))

ans = int(expression[0]) if expression[0] else 0

ans -= sum(map(int, expression[1:]))

print(ans)
