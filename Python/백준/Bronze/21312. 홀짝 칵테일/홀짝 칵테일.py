from functools import reduce


seq = list(map(int, input().split()))

odd = []

for i in seq:
    if i % 2:
        odd.append(i)

a = 0
b = 0

if odd:
    print(reduce(lambda x, y: x*y, odd))


else:
    print(reduce(lambda x, y: x*y, seq))
