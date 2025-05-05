from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    orders = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    arr = deque(arr)

    if n == 0:
        arr = deque()
    rev = False

    for order in orders:
        if order == "R":
            rev = not rev

        else:
            if len(arr) == 0:
                print("error")
                break
            if rev:
                arr.pop()
            else:
                arr.popleft()
    else:
        if rev:
            arr.reverse()
        print("[" + ",".join(arr) + "]")
