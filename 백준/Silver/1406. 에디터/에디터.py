import sys
input = sys.stdin.readline
print=sys.stdout.write

left = list(input().strip())
right = []

for _ in range(int(input())):
    o, *c = input().split()
    if o == 'L':
        if left:
            right.append(left.pop())
    elif o == 'D':
        if right:
            left.append(right.pop())
    elif o == 'B':
        if left:
            left.pop()
    elif o == 'P':
        left.append(c[0])

print(''.join(left + right[::-1])+"\n")