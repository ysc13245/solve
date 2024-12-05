from collections import deque


n, m = map(int, input().split())
order = list(map(int, input().split()))

lis = deque(range(1, n + 1))
cnt = 0
t = 0

for cur in order:
    back = n - lis.index(cur) - t
    front = lis.index(cur)
    if front >= back:
        cnt += back
        lis.rotate(back)
    else:
        cnt += front
        lis.rotate(-front)
    lis.popleft()
    t += 1
print(cnt)
