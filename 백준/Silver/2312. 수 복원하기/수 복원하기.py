from collections import defaultdict
import sys

input = sys.stdin.readline
print = sys.stdout.write


def primes_less(n):
    primes = [0] * 2 + [1] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            j = 2
            while i * j <= n:
                primes[i * j] = 0
                j += 1

    return [i for i in range(1, n + 1) if primes[i]]


lis = [int(input()) for _ in range(int(input()))]
primes = primes_less(max(lis))

for e in lis:
    answer = defaultdict(int)
    temp = e
    for p in primes:
        if p > temp:
            break
        while not temp % p:
            answer[p] += 1
            temp //= p

    # 소인수분해 결과 출력
    for x, y in answer.items():
        print(" ".join(map(str, [x, y])) + "\n")
