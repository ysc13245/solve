
def sol():
    def is_square(x: int):
        import math

        return math.isqrt(x) ** 2 == x

    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = [input().rstrip() for _ in range(n)]

    ans = -1

    for r in range(n):
        for c in range(m):
            for dy in range(-n + 1, n):
                for dx in range(-m + 1, m):
                    if dy == dx == 0:
                        x = int(arr[r][c])
                        if is_square(x):
                            ans = max(ans, x)
                    else:
                        num = 0
                        tx, ty = r, c
                        while 0 <= tx < n and 0 <= ty < m:
                            num = num * 10 + int(arr[tx][ty])
                            if is_square(num):
                                ans = max(ans, num)
                            tx += dy
                            ty += dx

    print(ans)


sol()
