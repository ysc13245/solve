import sys

input = sys.stdin.readline
print = sys.stdout.write


def dfs(depth, start):
    if depth == 6:
        print(" ".join(map(str, iarr)) + "\n")
        return

    for i in range(start, n):
        iarr.append(arr[i])
        dfs(depth + 1, i + 1)
        iarr.pop()


while True:
    n, *arr = list(map(int, input().split()))
    if n == 0:
        break

    iarr = []
    dfs(0, 0)
    print("\n")
