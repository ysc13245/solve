import sys

input = sys.stdin.readline

for _ in range(int(input())):
    sound = input().rstrip().split()
    cry = set()

    while True:
        s = input().rstrip()
        if s == "what does the fox say?":
            print(" ".join(x for x in sound if x not in cry))
            break
        cry.add(s.split()[-1])
