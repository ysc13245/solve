def solution():
    for i in range(int(input())):
        standard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if i!=0: input()
        board = [list(map(int, input().split())) for _ in range(9)]


        if any(sorted(row) != standard for row in board):
            print(f"Case {i+1}: INCORRECT")
            continue

        if any(sorted(board[row][col] for row in range(9)) != standard for col in range(9)):
            print(f"Case {i+1}: INCORRECT")
            continue

        if any(sorted(board[r+i][c+j] for i in range(3) for j in range(3)) != standard for r in [0, 3, 6] for c in [0, 3, 6]):
            print(f"Case {i+1}: INCORRECT")
            continue

        print(f"Case {i+1}: CORRECT")

solution()