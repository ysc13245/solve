import sys

input = sys.stdin.readline
print = sys.stdout.write


def sol():
    m, n = map(int, input().split())
    seq = list(map(int, input().split()))
    summed = [0]

    for i in range(m):
        summed.append(summed[-1] + seq[i])

    for _ in range(n):
        l, r = map(int, input().split())
        print(str(summed[r] - summed[l - 1]) + "\n")


sol()
