def sol():
    import sys

    input = sys.stdin.readline
    n = int(input())
    cow = sorted(list(map(int, input().split())) for _ in range(n))
    cnt = 0

    for start, duration in cow:
        cnt = max(cnt, start) + duration

    print(cnt)


sol()
