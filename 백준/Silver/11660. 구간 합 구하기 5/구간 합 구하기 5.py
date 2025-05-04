import sys

input = sys.stdin.readline
print = sys.stdout.write


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

summed = [[0] * (n + 1) for _ in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, n + 1):
        summed[i][j] = (
            summed[i][j - 1]
            + summed[i - 1][j]
            - summed[i - 1][j - 1]
            + arr[i - 1][j - 1]
        )

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    ans = (
        summed[x2][y2]
        - summed[x1 - 1][y2]
        - summed[x2][y1 - 1]
        + summed[x1 - 1][y1 - 1]
    )

    print(str(ans) + "\n")
