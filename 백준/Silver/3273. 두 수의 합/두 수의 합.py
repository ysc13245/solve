n = int(input())

seq = sorted(list(map(int, input().split())))
t = int(input())
cnt = 0
l, r = 0, len(seq) - 1

while l < r:
    summed = seq[l] + seq[r]
    if summed == t:
        cnt += 1
        l += 1
    elif summed < t:
        l += 1
    else:
        r -= 1

print(cnt)
