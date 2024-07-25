import calendar


def solution():
    import sys

    input=sys.stdin.readline
    calendar = [0] * 71
    schedule = {}
    n = int(input())
    for _ in range(n):
        name, *args = input().split()

        schedule[name] = list(map(int,args))

    for _ in range(n):
        name, balance = input().split()

        if schedule[name][2]<=int(balance):
            calendar[(schedule[name][0]-1)*7 + schedule[name][1]] = 1
    
    max_cnt = 0
    cnt = 0

    for m in calendar:
        if m:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    
    print(max_cnt)



solution()
 