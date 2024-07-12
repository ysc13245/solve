from collections import deque

for _ in range(int(input())):
    
    N, M = map(int,input().split())
    queue = deque(map(lambda x: [int(x),False],input().split()))
    queue[M][1] = True
    result = []
    while queue:
        if queue[0][0] == max(x[0] for x in queue):
            if queue[0][1]:

                print(len(result)+1)
                break
            result.append(queue.popleft())
        else:
            queue.append(queue.popleft())
    else:
        print(len(result))