n, m = map(int, input().split())

ls = [list(map(int, input().split())) for _ in range(n)]
mx_ls = []
for i in range(m):
    for j in range(i+ 1, m):
        for k in range(j+ 1, m):
            mx_ls.append(sum(max(r[i], r[j], r[k]) for r in ls))
print(max(mx_ls))
