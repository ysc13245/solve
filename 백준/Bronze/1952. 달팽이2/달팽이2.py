dir = 0
m, n = map(int, input().split())
canvas = [[0 for _ in range(n)] for _ in range(m)]
cur = [0, 0]
cnt = 0

while cnt < 2:
    canvas[cur[0]][cur[1]] = 1
    next = list(cur)

    match dir % 4:
        case 0:
            next[1] += 1
        case 1:
            next[0] += 1
        case 2:
            next[1] -= 1
        case 3:
            next[0] -= 1

    if next[0] < m >=0 and next[1] < n>=0 and canvas[next[0]][next[1]] == 0:
        cnt=0
        cur = list(next)
    else:
        cnt += 1
        dir += 1
print(dir-2)
