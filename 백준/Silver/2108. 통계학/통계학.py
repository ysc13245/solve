from collections import Counter

lis = sorted(list(map(int,open(0).readlines()[1:])))
dic = Counter(lis)
max_n = max(dic.values())

print(round(sum(lis)/len(lis)))
print(lis[len(lis)//2])
print(max(sorted([x for x, y in dic.items() if y==max_n])[:2]))
print(lis[-1]-lis[0])
