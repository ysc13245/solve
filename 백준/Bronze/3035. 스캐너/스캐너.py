def sol():
    ans = []
    _, _, r, c, *scan = open(0).read().split()
    r,c = map(int, (r,c))
    for row in scan:
        for _ in range(r):
            ans.append("")
            for col in row:
                    ans[-1] += c * col
    print("\n".join(ans))


sol()
