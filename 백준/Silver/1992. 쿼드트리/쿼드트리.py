def pack(board):
    c = board[0][0]
    if all(board[i][j] == c for i in range(len(board)) for j in range(len(board))):
        print(c)
        return

    half = len(board) // 2
    print("(")
    pack([row[:half] for row in board[:half]])
    pack([row[half:] for row in board[:half]])
    pack([row[:half] for row in board[half:]])
    pack([row[half:] for row in board[half:]])
    print(")")


import sys

input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
board = [input().rstrip() for _ in range(n)]

pack(board)