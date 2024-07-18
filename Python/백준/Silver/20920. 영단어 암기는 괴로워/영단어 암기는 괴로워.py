def solution():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    words = defaultdict(int)
    N, M = map(int, input().split())
    for _ in range(N):
        s = input().rstrip()
        if len(s) >=M:
            words[s] += 1

    print(*sorted(words.keys(), key=(lambda x: (-words[x], -len(x), x))), sep="\n")
    
solution()
