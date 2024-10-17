from collections import deque

N = int(input())
table = [i for i in range(1, N + 1)]
hand = deque()
techs = list(map(int, input().split()))[::-1]

for i, card in enumerate(table):
    match techs[i]:
        case 1:
            hand.append(card)
        case 2:
            temp = hand.pop()
            hand.append(card)
            hand.append(temp)
        case 3:
            hand.appendleft(card)
print(*list(hand)[::-1])

