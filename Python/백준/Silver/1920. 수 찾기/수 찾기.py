import sys

input = sys.stdin.readline
print = sys.stdout.write


def solution():
    input()
    sequence = set(map(int, input().split()))

    n = int(input())
    for i in map(int, input().split()):
        print(str(int(i in sequence)) + "\n")


solution()
