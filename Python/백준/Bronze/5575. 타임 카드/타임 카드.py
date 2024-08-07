seq = open(0).readlines()
for case in seq:
    case = list(map(int, case.split()))
    s = case[0] * 3600 + case[1] * 60 + case[2]
    e = case[3] * 3600 + case[4] * 60 + case[5]
    ans = e - s
    print(f"{ans//3600} {(ans % 3600) // 60} {ans%60}")
