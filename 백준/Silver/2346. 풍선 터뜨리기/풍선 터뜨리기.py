from collections import deque


n = int(input())
lis = list(map(int, input().split()))

deque = deque([[i + 1, lis[i]] for i in range(len(lis))])
answer = []

while deque:
    idx, num = deque.popleft()
    answer.append(idx)
    if deque:
        deque.rotate(-(num-1) if num > 0 else -num)

print(*answer)
