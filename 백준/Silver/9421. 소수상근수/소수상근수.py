def is_sangun(num):
    visited = set()
    while num != 1 and num not in visited:
        visited.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

n = int(input())
ans = []
primes = [True] * (n + 1)
primes[0:2] = [False] * 2

for i in range(2, int(pow(n, 0.5)) + 1):
    if primes[i]:
        for j in range(i * i, n + 1, i):
            primes[j] = False


for i in range(2, n + 1):
    if primes[i] and is_sangun(i):
        ans.append(i)

print(*ans, sep="\n")
