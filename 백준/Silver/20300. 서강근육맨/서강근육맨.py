n = int(input())
l = sorted(list(map(int, input().split())))

if n % 2:
    print(max(max((l[i] + l[-i-2] for i in range(n//2)), default=0), l[-1]))

else:
    print(max(l[i] + l[-i-1] for i in range(n//2)))
