m , n = map(int,input().split())
ver = {"d":"b", "b":"d", "q":"p", "p":"q"}
hor = {"d":"q", "b":"p", "q":"d", "p":"b"}
ans = ""
for _ in range(m):
    if n==2:
        print("".join(ver[x] for x in input()))
    else:
        print("".join(hor[x] for x in input()))
