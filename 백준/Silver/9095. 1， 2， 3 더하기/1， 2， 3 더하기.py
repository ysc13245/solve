for _ in range(int(input())):
    seq = [1, 2, 4]
    N = int(input())
    if N < 4:
        print(seq[N - 1])
    else:
        for i in range(N-3):
            seq.append(seq.pop(0) + seq[0] + seq[1])
        print(seq[-1])
