print(*map(lambda x: bin(x)[2:], [int(x, 2) + int(y, 2) for x, y in [input().split() for _ in range(int(input()))]]), sep="\n")
