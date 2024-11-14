def sol():
    n, score, p = map(int, input().split())
    if not n:
        print(1)
        return

    seq = sorted(list(map(int, input().split())), reverse=True)
    rank = [n for n in seq if n >= score]
    l = len(rank)

    if l >= p:
        print(-1)
        return
    cnt = 0
    for n in rank[::-1]:
        if n > score:
            break
        cnt += 1

    print(l - cnt + 1)
    return


sol()
