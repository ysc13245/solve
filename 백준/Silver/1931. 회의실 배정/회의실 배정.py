def solution():
    import sys
    
    input = sys.stdin.readline
    schedule=[]
    
    schedule = [list(map(int, input().split())) for _ in range(int(input()))]
    schedule.sort(key=lambda x: (x[1], x[0]))
    t = 0
    cnt = 1
    for i, x in enumerate(schedule[1:]):
        if schedule[t][1] <= x[0]:
            cnt += 1
            t = i+1
    return cnt
print(solution())
 