import sys

input=sys.stdin.readline

for _ in range(int(input())):
    M, N = map(int, input().split())

    board = [list(map(int, input().split())) for  _ in range(M)]
    cnt = 0

    for i in range(M):
        for j in range(N):
            if board[i][j]:
                cnt+=(sum(1 for k in range(i + 1, M) if board[k][j] == 0))
    print(cnt)