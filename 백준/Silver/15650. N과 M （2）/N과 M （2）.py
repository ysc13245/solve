def solution():
    from itertools import combinations

    N,M = map(int,input().split())

    for x in combinations(range(1,N+1),M):
        print(*x)


solution()