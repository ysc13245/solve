lis = map(int, open(0).readlines()[:-1])
seq = [0] * 2 + [1] * (1000000 - 1)

for i in range(2, 1001):
    if seq[i]:
        for j in range(i * i, 1000000, i):
            seq[j] = 0

primes = [i for i in range(3, 1000000) if seq[i]]
answer = []

for n in lis:
    for pn in primes:
        if seq[n - pn]:
            answer.append(f"{n} = {pn} + {n - pn}")
            break


print("\n".join(answer))