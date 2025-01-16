lis = sorted(list(map(int, open(0).readlines()[1].split())))
ans = sum(0.5 * n for n in lis) + 0.5 * lis[-1]
print(int(ans) if ans.is_integer() else ans)