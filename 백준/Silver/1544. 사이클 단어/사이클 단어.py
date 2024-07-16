def solution():
    import sys

    input = sys.stdin.readline
    words = [input().rstrip() for _ in range(int(input()))]
    cnt = 0
    circle = set()

    for word in words:
        if word in circle:
            continue

        cnt += 1
        for i in range(len(word)):
            circle.add(word[i:]+ word[:i])

    print(cnt)

solution()
