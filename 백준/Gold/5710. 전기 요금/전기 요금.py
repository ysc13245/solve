import sys

input = sys.stdin.readline

def solution():
    def tcost_to_tpower(total_cost):
        if total_cost <= 200:
            return total_cost // 2
        elif total_cost <= 29_900:
            return (total_cost - 200) // 3 + 100
        elif total_cost <= 4_979_900:
            return (total_cost - 29_900) // 5 + 10_000
        else:
            return (total_cost - 4_979_900) // 7 + 1_000_000

    def cost(power):
        if power <= 100:
            return power * 2
        elif power <= 10_000:
            return 100 * 2 + (power - 100) * 3
        elif power <= 1_000_000:
            return 100 * 2 + 9_900 * 3 + (power - 10_000) * 5
        else:
            return 100 * 2 + 9_900 * 3 + 990_000 * 5 + (power - 1_000_000) * 7

    while True:
        A, B = map(int, input().strip().split())
        if A == 0 and B == 0:
            break

        total_power = tcost_to_tpower(A)

        left, right = 1, total_power - 1
        result = 0

        while left <= right:
            my = (left + right) // 2
            neighbor = total_power - my

            my_cost = cost(my)
            neighbor_cost = cost(neighbor)
            diff = neighbor_cost - my_cost

            if diff == B:
                result = my_cost
                break
            elif diff < B:
                right = my - 1
            else:
                left = my + 1

        print(result)

solution()