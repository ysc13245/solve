import sys

pattern = [[str(i**j % 10) for j in range(1, 5)] for i in range(1, 10)]+[["10"]*4]
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(pattern[(a - 1) % 10][(b - 1) % 4] + "\n")
