n = int(input())
a = list(map(int, input().split()))
p = {i: k for k, i in enumerate(sorted(range(n), key=lambda i: (a[i], i)))}
print(*[p[i] for i in range(n)])