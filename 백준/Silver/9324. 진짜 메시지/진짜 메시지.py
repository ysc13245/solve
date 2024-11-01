from collections import defaultdict

for _ in range(int(input())):
    s = input()
    counter = defaultdict(int)

    for i, c in enumerate(s):
        counter[c] += 1
        if counter[c] == 3:
            try:
                if s[i + 1] != c:
                    print("FAKE")
                    break
                counter[c] = -1
            except:
                print("FAKE")
                break
    else:
        print("OK")
