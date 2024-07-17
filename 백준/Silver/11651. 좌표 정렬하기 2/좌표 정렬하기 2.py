def solution():
    import sys
    lis = []
    for _ in range(int(input())):
        lis.append(list(map(int,input().split())))
    
    lis.sort(key=lambda x: (x[1], x[0]))
    
    for x in lis:
        print(*x)

solution()
