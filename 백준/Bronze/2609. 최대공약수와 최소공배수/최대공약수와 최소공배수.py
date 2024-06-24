def gcd(a, b):
    """두 수의 최대공약수 구하는 함수"""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """두 수의 최소공배수 구하는 함수"""
    return abs(a * b) // gcd(a, b)


a, b = map(int,input().split())
print(gcd(a, b))
print(lcm(a, b))