import sys

input = sys.stdin.readline
print = sys.stdout.write

lis = list(map(int, open(0)))[1:]


def primes_less(n):
    primes = [0] * 2 + [1] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            j = 2
            while i * j <= n:
                primes[i * j] = 0
                j += 1

    return primes


primes = primes_less(max(lis))
for n in lis:
    for p in range(n // 2, 1, -1):
        if primes[p] and primes[n - p]:
            print(str(p) + " " + str(n - p) + "\n")
            break
