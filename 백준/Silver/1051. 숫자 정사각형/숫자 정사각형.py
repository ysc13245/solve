import sys

input = sys.stdin.readline
n, m = map(int, input().split())
seq = [input().rstrip() for _ in range(n)]
ans = [1]

for i in range(n):
    idx = {}
    for j in range(m):
        idx[seq[i][j]] = idx.get(seq[i][j], []) + [j]

    for lis in [x for x in idx.values() if len(x) >= 2]:
        for k in range(len(lis) - 1):
            for l in range(k + 1, len(lis)):
                diff = lis[l] - lis[k]
                
                if i + diff < n and seq[i][lis[k]] == seq[i + diff][lis[k]] == seq[i + diff][lis[l]]:
                    ans.append(diff + 1)

print(max(ans) ** 2)