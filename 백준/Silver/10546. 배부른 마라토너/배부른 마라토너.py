def solution():
    import sys

    input=sys.stdin.readline
    seq = {}
    
    for _ in range(int(input())*2-1):
        x = input()

        try:
            del seq[x]
        except:
            seq[x] = True

    print(next(iter(seq.keys())).rstrip())

solution()
