import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
max_value = max(map(max, board))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def dfs(x, y, count, total):
    global answer
    
    if total + (4 - count) * max_value <= answer:
        return
    
    if count == 4:
        answer = max(answer, total)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, count + 1, total + board[nx][ny])
            visited[nx][ny] = False

def check(x, y):
    global answer
    

    if x > 0 and y > 0 and y < m - 1:
        total = board[x][y] + board[x-1][y] + board[x][y-1] + board[x][y+1]
        answer = max(answer, total)
    
    if x < n - 1 and y > 0 and y < m - 1:
        total = board[x][y] + board[x+1][y] + board[x][y-1] + board[x][y+1]
        answer = max(answer, total)

    if x > 0 and x < n - 1 and y > 0:
        total = board[x][y] + board[x-1][y] + board[x+1][y] + board[x][y-1]
        answer = max(answer, total)
    
    if x > 0 and x < n - 1 and y < m - 1:
        total = board[x][y] + board[x-1][y] + board[x+1][y] + board[x][y+1]
        answer = max(answer, total)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        
        check(i, j)

print(answer)