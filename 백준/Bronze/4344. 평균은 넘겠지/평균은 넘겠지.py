for _ in range(int(input())):
    scores = list(map(int,input().split()))[1:]
    avg = sum(scores) / len(scores)
    print(f"{round(sum(1 for x in scores if x>avg)/len(scores)*100,3)}%")