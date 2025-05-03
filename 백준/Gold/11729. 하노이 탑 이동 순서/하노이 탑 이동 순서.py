def hanoi(num, start, end):
    if num == 1:
        ans.append(f"{start} {end}")
        return

    hanoi(num - 1, start, 6 - start - end)
    ans.append(f"{start} {end}")
    hanoi(num - 1, 6 - start - end, end)


n = int(input())

ans = [str(2**n - 1)]
hanoi(n, 1, 3)
print("\n".join(ans))
