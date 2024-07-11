input = open(0).readlines()[1:]

iarr = []

for x in range(ord('a'), ord("z")+1):
    input = [yy.replace(chr(x), " ") for yy in input]


input = sum(list(map(lambda x: list(map(int,x.split())), input)),[])
print("\n".join(map(str,sorted(input))))
