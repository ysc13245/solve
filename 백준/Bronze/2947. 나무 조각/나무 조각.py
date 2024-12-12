seq = list(map(int, input().split()))
l = len(seq)
for i in range(l - 1):
    for j in range(l - 1 - i):
        if seq[j] > seq[j + 1]:
            seq[j : j + 2] = [seq[j + 1], seq[j]]
            print(*seq)
