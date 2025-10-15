n, l, w, h = map(int, input().split())
s, e = 0, max(l, w, h)

for _ in range(10000):
    M = (s + e) / 2
    count = (l // M) * (w // M) * (h // M)
    if count >= n:
        s = M
    else:
        e = M

print(s)
