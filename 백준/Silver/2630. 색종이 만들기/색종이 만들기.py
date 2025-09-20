import sys


def is_uniform(x, y, n):
    color = canvas[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if canvas[i][j] != color:
                return False
    return color


def div(x, y, n):
    color = is_uniform(x, y, n)
    if color is not False:
        if color == 1:
            result[0] += 1
        else:
            result[1] += 1
        return

    m = n // 2
    div(x, y, m)
    div(x + m, y, m)
    div(x, y + m, m)
    div(x + m, y + m, m)


input = sys.stdin.readline
n = int(input())
result = [0, 0]
canvas = [list(map(int, input().split())) for _ in range(n)]
div(0, 0, n)

print(result[1])
print(result[0])
