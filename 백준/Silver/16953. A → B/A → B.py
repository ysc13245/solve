
def sol():
    a, b = map(int, input().split())
    cnt = 1
    while b > a:
        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2
        else:
            print(-1)
            return
        cnt += 1

    print(cnt if b == a else -1)


sol()
