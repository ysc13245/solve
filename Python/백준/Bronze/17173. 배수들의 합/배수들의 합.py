n, m, *k = map(int, input().split())
k = list(map(int, input().split()))
print(sum(i for i in range(1, n + 1) if any(i % j==0 for j in k)))
