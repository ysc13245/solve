import sys

input=sys.stdin.readline
homework = []
score = 0

for _ in range(int(input())):
    if (s := input()) != "0\n":
        homework.append(list(map(int,s.split()[1:])))

    if homework:
        homework[-1][-1] -= 1
        if homework[-1][-1] == 0:
            score += homework[-1][0]
            homework.pop()

print(score)