from collections import Counter


for i in range(int(input())):
    input()
    res = Counter("o" if n % 2 else "e" for n in map(int, input().split()))

    print("amsminn" if res["o"] != res["e"] and max(res.values()) % 2 else "heeda0528")