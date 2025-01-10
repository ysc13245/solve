from decimal import Decimal, getcontext

getcontext().prec = 1000
a, b = map(Decimal, input().split())
print(a/b)