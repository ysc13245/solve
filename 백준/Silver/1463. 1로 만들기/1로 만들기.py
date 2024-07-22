def solution():
    import sys

    input = sys.stdin.readline
    n = int(input())

    if n==1:
        print(0)
        return
    
    seq = [1,1,1] + [0]*(n-3)

    for i in range(3, n):

        temp=[]
        temp.append(seq[i - 1] + 1)

        if (i+1) % 2 == 0:
            temp.append(seq[i // 2] + 1)

        if (i+1) % 3 == 0:
            temp.append(seq[i // 3] + 1)
        seq[i] = min(temp)

    
    print(seq[-1])

solution()
