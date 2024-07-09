input = open(0).readlines()[1:]
sum=0
for x in input:
    sum += 1 if x.count("O")>x.count("X") else 0
print(sum)