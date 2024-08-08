import sys

input = sys.stdin.readline

fri = {1: 0, 2: 0, 3: 0}

for _ in range(int(input())):
    s = input()
    match s:
        case "1/4\n":
            fri[1] += 1
        case "1/2\n":
            fri[2] += 1
        case "3/4\n":
            fri[3] += 1
pizza = fri[3]
fri[1]= max(0, fri[1]-pizza)

pizza += fri[2] // 2
fri[2] %= 2
if fri[2]:
    pizza += 1
    fri[1] = max(fri[1] - 2, 0)
pizza += (fri[1]+3) //4
print(pizza)