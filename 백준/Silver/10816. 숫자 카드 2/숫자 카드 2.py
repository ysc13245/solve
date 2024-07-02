from collections import defaultdict

cards = defaultdict(int)

input()
for x in input().split():
    cards[x] += 1

input()

print(" ".join(str(cards[x]) for x in input().split()))