def solution():
    from collections import Counter

    counter = Counter(input())
    odd = []
    even = []

    for k, v in counter.items():
        if v % 2:
            odd.append(k)
        else:
            even.append(k)

    if len(odd) > 1:
        print("I'm Sorry Hansoo")
        return

    half = "".join(counter[c] // 2 * c for c in sorted(odd + even))

    print(half + odd[0] + half[::-1] if odd else half + half[::-1])


solution()
