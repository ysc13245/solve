def primes_less(m, n):
    primes = [0] * 2 + [1] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            j = 2
            while i * j <= n:
                primes[i * j] = 0
                j += 1

    return [i for i in range(m, n+1) if primes[i]]


print(*primes_less(*list(map(int,input().split()))),sep="\n")