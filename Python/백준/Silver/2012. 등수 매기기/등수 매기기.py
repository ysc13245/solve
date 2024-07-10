input = sorted(list(map(int,open(0).readlines()[1:])))

print(sum([abs(i-input[i]+1) for i in range(len(input))]))
