def sol():
    seq = [(1, 0), (0, 1)]
    lis = list(map(int, open(0).readlines()[1:]))
    for _ in range(max(lis)):
        seq.append(tuple(sum(e) for e in zip(seq[-1], seq[-2])))

    print(*[" ".join(map(str,seq[n])) for n in lis], sep="\n")


sol()
