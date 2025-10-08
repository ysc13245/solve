n = int(input())
m = int(input())

arr = []
if m:
    arr = list(map(int, input().split()))

ans = abs(n - 100)

for i in range(1000001):
    if not any(int(digit) in arr for digit in str(i)):
        ans = min(ans, len(str(i)) + abs(i - n))

print(ans)