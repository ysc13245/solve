sig = [
    "053421",
    "31",
    "03642",
    "03612",
    "5631",
    "05612",
    "054216",
    "031",
    "0123456",
    "05361",
]

sig = ["".join("1" if i in map(int, e) else "0" for i in range(7))[::-1] for e in sig]

num = list(map(lambda x: str(int(x, 2)).zfill(3), sig))

while True:
    s = input()
    if s == "BYE":
        break
    a, b = s[:-1].split("+")
    a = int("".join(map(str,[num.index(a[i : i + 3]) for i in range(0, len(a), 3)])))
    b = int("".join(map(str,[num.index(b[i : i + 3]) for i in range(0, len(b), 3)])))
    ans = list(str(a + b))
    print(s+"".join(num[int(c)] for c in ans))