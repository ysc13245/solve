import sys

input=sys.stdin.readline
print=sys.stdout.write

n, m = map(int, input().split())
girlgroup = {}

for _ in range(n):
    group = input()
    girlgroup[group] = []
    for _ in range(int(input())):
        girlgroup[group].append(input())
    girlgroup[group].sort()

for _ in range(m):
    quiz = input()
    if int(input()):
        for k, v in girlgroup.items():
            if quiz in v:
                print(k)
                break
    else:
        print("".join(girlgroup[quiz]))
