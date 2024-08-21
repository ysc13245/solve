import sys

input=sys.stdin.readline
print=sys.stdout.write

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    population = [list(range(1, n + 1))]

    for _ in range(k):
        population.append([sum(population[-1][:i]) for i in range(1, n + 1)])

    print(str(population[k][n-1])+"\n")