def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


import math

input()

n = math.prod({i for i in map(int, set(input().split())) if is_prime(i)})
print(n if n != 1 else -1)
