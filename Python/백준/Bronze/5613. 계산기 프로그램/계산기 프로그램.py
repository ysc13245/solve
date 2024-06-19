import sys

input = sys.stdin.readline
a = int(input())
while True:
    op = input()
    if op == '=\n':
        break
    b = int(input())
    if op == '+\n':
        a += b
    elif op == '-\n':
        a -= b
    elif op == '*\n':
        a *= b
    elif op == '/\n':
        a //= b
print(a)