n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [1 if i+1 in arr else 0 for i in range(max(arr))]

cnt=0
for i in range(len(arr2)):
  if arr2[i]:
    arr2[i:i+m] = [0]*m
    cnt+=1

print(cnt)