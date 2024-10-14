n, x = map(int, input().split())
visitor = list(map(int, input().split()))
summed = [0]

for i in visitor:
    summed.append(summed[-1] + i)


visitors = []
for i in range(n - x + 1):
    visitors.append(summed[i + x] - summed[i])
max = max(visitors)
if max:
    print(max)
    print(visitors.count(max))
else:
    print("SAD")
