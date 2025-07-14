import sys


def sol():
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return True

        if rank[x] > rank[y]:
            parent[y] = x

        elif rank[x] < rank[y]:
            parent[x] = y

        else:
            parent[y] = x
            rank[x] += 1

        return False

    def is_union(x, y):
        return str(int(find(x) == find(y)))

    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline
    print = sys.stdout.write
    for i in range(int(input())):
        n = int(input())
        parent = [i for i in range(n)]
        rank = [0] * (n)

        for _ in range(int(input())):
            union(*map(int, input().split()))

        print(f"Scenario {i + 1}:\n")
        for _ in range(int(input())):
            print(is_union(*map(int, input().split())) + "\n")
        print("\n")


sol()
