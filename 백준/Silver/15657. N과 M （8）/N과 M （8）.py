def sol():
    import sys

    input = sys.stdin.readline
    print = sys.stdout.write

    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))

    stack = [(0, [])]

    while stack:
        idx, arr = stack.pop()

        if len(arr) == m:
            print(" ".join(map(str, arr))+"\n")
            continue

        for i in range(n - 1, idx - 1, -1):
            stack.append((i, arr + [nums[i]]))

sol()