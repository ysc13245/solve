def solution():
    from itertools import count


    n = input()
    idx = 0
    nl = len(n)
    i = 0
    for i in count(1):
        for c in str(i):
            if n[idx] == c:
                idx += 1
                if idx >= nl:
                    break
        else:
            continue
        break
    print(i)

solution()