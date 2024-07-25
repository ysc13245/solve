def solution():
    from math import lcm, gcd

    num = [list(map(int, input().split())) for _ in range(2)]
    lcm = lcm(num[0][1], num[1][1])
    num = list(map(lambda x: [x[0] * (lcm // x[1]), x[1]], num))
    num[0][1], num[1][1] = lcm, lcm
    result = [num[0][0] + num[1][0], lcm]

    print(*list(map(lambda x: x // gcd(result[0], result[1]), result)))


solution()
