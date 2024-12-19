n, k = map(int, input().split())
seq = list(map(int, input().split()))

summed = [sum(seq[:k])]
for i in range(n - k):
    summed.append(summed[i] - seq[i] + seq[i + k])

print(max(summed))
