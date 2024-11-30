def sol():
    import sys

    input = sys.stdin.readline
    print = sys.stdout.write

    n, m = map(int, input().split())
    grades = [(x[0], int(x[1])) for x in (input().split() for _ in range(n))]
    for _ in range(m):
        score = int(input())
        start, end = 0, n - 1

        while start <= end:
            mid = (start + end) // 2

            if grades[mid][1] >= score:
                end = mid - 1
            else:
                start = mid + 1
        print(grades[start][0]+"\n")


sol()
