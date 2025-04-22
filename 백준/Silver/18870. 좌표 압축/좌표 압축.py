input()
arr = list(map(int, input().split()))
dic = {v: i for i, v in enumerate(sorted(set(arr)))}
print(*(dic[n] for n in arr))
