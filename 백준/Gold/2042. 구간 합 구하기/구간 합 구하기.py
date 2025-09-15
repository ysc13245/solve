import sys

input = sys.stdin.readline
print = sys.stdout.write
n, m, k = map(int, input().split())

arr = [0] * (n + 1)
tree = [0] * (n + 1)


def update(i, v):
    while i <= n:
        tree[i] += v
        i += i & -i


def prefix_sum(i):
    summed = 0
    while i > 0:
        summed += tree[i]
        i -= i & -i
    return summed


def range_sum(start, end):
    return str(prefix_sum(end) - prefix_sum(start - 1))+"\n"


for i in range(1, n + 1):
    num=int(input())
    arr[i]=num
    update(i,num)

for i in range(m+k):
    o,a,b=map(int,input().split())
    if o==1:
        update(a,b-arr[a])
        arr[a]=b
    else:
        print(range_sum(a,b))