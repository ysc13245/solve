def sol():
    from collections import deque
    import sys

    input = sys.stdin.readline

    arr = [deque(input().rstrip()) for _ in range(4)]
    k = int(input())

    for _ in range(k):
        idx, dir = map(int, input().split())
        idx -= 1

        dirs = [0] * 4
        dirs[idx] = dir

        for i in range(idx - 1, -1, -1):

            if arr[i][2] != arr[i + 1][6]:
                dirs[i] = -dirs[i + 1]

            else:
                break

        for i in range(idx + 1, 4):

            if arr[i - 1][2] != arr[i][6]:
                dirs[i] = -dirs[i - 1]

            else:
                break

        for i in range(4):
            arr[i].rotate(dirs[i])

    ans = sum(1 << i for i in range(4) if arr[i][0] == "1")
    
    print(ans)



sol()
