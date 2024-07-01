import sys

input = sys.stdin.readline

M, N = map(int, input().split())
board = [input() for _ in range(M)]

standard = ["BW" * 4 if _ % 2 else "WB" * 4 for _ in range(8)]
res = 64

for i in range(M-7):
    for j in range(N-7):
        temp = [row[j:j+8] for row in board[i:i+8]]
        cnt = 0
        for y in range(8):
            for x in range(8):
                cnt += 1 if temp[y][x] != standard[y][x] else 0
        res = min(res, cnt, 64-cnt)
print(res)