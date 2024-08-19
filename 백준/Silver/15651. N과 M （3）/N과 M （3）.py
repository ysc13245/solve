import sys
import itertools
print=sys.stdout.write

n, m = map(int, input().split())
for x in itertools.product(range(1, n+1),repeat=m):
    print(" ".join(map(str,x))+"\n")