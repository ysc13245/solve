n = int(input())
lis = list(map(int, input().split()))

i = 0
answer = [1]

for _ in range(n - 1):
    q = lis[i % n]
    lis[i % n] = 0
    for _ in range(abs(q)):
        i += 1 if q > 0 else -1
        while not lis[i % n]:
            i += 1 if q > 0 else -1
    answer.append(i % n + 1)

print(*answer)