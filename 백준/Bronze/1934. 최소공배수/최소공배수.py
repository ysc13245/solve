from math import lcm
print(*list(map(lambda x: lcm(*map(int, x.split())), open(0).readlines()[1:])))