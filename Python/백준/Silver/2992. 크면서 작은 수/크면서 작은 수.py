def solution():
    from itertools import permutations
    from math import log10
    
    n = int(input())
    answer=["0"]
    for x in permutations(sorted(list(str(n))),int(log10(n))+1):
        if int("".join(x))>n:
            answer = x
            break
    print("".join(answer))


solution()
