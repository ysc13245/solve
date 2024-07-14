def solution():
    data = [int(input()) for _ in range(7)]
    data = [x for x in data if x % 2]
    print(str(sum(data))+"\n"+str(min(data)) if sum(data)!= 0 else -1)
solution()
