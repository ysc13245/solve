def solution():
    import sys

    input = sys.stdin.readline
    print = sys.stdout.write

    n = int(input())
    lis = list(map(int, input().split()))
    summed = [0]
    for n in lis:
        summed.append(summed[-1] + n)

    for _ in range(int(input())):
        n, m = map(int, input().split())
        print(str(summed[m] - summed[n - 1]) + "\n")


solution()
