N, K = map(int, input().split())

cats = sorted(list(map(int, input().split())), reverse=True)
L, R = 0, N-1
cnt = 0

while L<R:
    if cats[L]+cats[R]<=K:
        L+=1
        R-=1
        cnt += 1
    else:
        L += 1
print(cnt)