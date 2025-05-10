import sys

print=sys.stdout.write

n, m = map(int, input().split())
arr = sorted(list(input().split()))
vowels = {"a", "e", "i", "o", "u"}


idxs = list(range(n))

while True:
    vowel_cnt = 0
    consonant_cnt = 0
    code = []
    for idx in idxs:
        ch = arr[idx]
        code.append(ch)
        if ch in vowels:
            vowel_cnt += 1
        else:
            consonant_cnt += 1

    if vowel_cnt >= 1 and consonant_cnt >= 2:
        print("".join(code)+"\n")

    for i in range(n - 1, -1, -1):
        if idxs[i] < m - n + i:
            idxs[i] += 1

            for j in range(i + 1, n):
                idxs[j] = idxs[j - 1] + 1
            break
    else:
        break
