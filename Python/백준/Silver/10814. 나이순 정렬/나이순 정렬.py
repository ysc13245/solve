arr=[]

for _ in range(int(input())):
    arr.append(input().split())
    
arr.sort(key=lambda x: int(x[0]))

for x in arr:
    print(x[0], x[1])