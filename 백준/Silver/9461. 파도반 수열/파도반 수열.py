import sys

input = sys.stdin.readline
print = sys.stdout.write

arr = [0, 1, 1, 1]

for i in range(4, 101):
    arr.append(arr[i - 2] + arr[i - 3])

for _ in range(int(input())):
    print(str(arr[int(input())]) + "\n")
