from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
apples = [[False] * n for _ in range(n)]

for _ in range(k):
    u, v = map(int, input().split())
    apples[u - 1][v - 1] = True

l = int(input())
commands = {int(x): y for _ in range(l) for x, y in [input().split()]}

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

head = (0, 0)
tail = deque([head])
dir = 0
t = 0

while True:
    t += 1
    head = (head[0] + dx[dir], head[1] + dy[dir])

    if not (0 <= head[0] < n and 0 <= head[1] < n):
        print(t)
        break

    if head in tail:
        print(t)
        break

    is_apple = apples[head[0]][head[1]]

    tail.append(head)

    if not is_apple:
        tail.popleft()

    apples[head[0]][head[1]] = False

    order = commands.get(t)
    if order == "L":
        dir = (dir - 1) % 4
    elif order == "D":
        dir = (dir + 1) % 4
