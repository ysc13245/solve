def sol():
    seq = [1,2]
    n = int(input())
    if n == 1:
        print(1)
        return
    for _ in range(n - 2):
        seq.append((seq.pop(0)+seq[0]) % 10007)
    print(seq[-1])
    return


sol()