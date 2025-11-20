def roll(o):
    global x, y

    match o:
        case 1:

            if y == m - 1:
                return False

            y += 1
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]

        case 2:

            if y == 0:
                return False

            y -= 1
            dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]

        case 3:

            if x == 0:
                return False

            x -= 1
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]

        case 4:

            if x == n - 1:
                return False

            x += 1
            dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]

    return True


n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0] * 6
for o in order:
    if roll(o) == False:
        continue

    if board[x][y]:
        dice[1] = board[x][y]
        board[x][y] = 0
    else:
        board[x][y] = dice[1]

    print(dice[0])
