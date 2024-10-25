import sys

input = sys.stdin.readline

n, m = map(int, input().split())
S = {input(): 1 for _ in range(n)}

print(sum(1 for e in (input() for e in range(m)) if S.get(e)))
