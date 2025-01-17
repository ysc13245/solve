N = int(input())

cnt = 0
l = r = summed=1
while l <= N / 2:
    if summed < N:
        r += 1
        summed += r
    elif summed > N:
        summed -= l
        l += 1
    else:
        cnt += 1
        summed -= l
        l += 1
        r += 1
        summed += r
print(cnt + 1)
