def solution():
    import sys

    input=sys.stdin.readline
    print= sys.stdout.write

    m ,n = map(int,input().split())
    queue = {input():i for i in range(n)}
    print("".join(sorted(queue.keys(), key=queue.get)[:m]))
    

solution()
 