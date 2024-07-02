import sys

input = sys.stdin.readline

cards = [0] * 20000001

input()
a = list(map(lambda x: int(x) + 10000000, input().split()))
for x in a:
    cards[x] += 1

input()
b = list(map(lambda x: int(x) + 10000000, input().split()))
print(*[cards[x] for x in b])
