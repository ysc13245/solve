def solution():
    import sys
    input = sys.stdin.readline
    li = list(map(int, [input() for _ in range(int(input()))]))

    stack, result = [], []
    n = 1

    for num in li:
        while n <= num:
            stack.append(n)
            result.append("+")
            n += 1

        if stack[-1] != num:
            return "NO"
        
        stack.pop()
        result.append("-")
        

    return "\n".join(result)


print(solution())
