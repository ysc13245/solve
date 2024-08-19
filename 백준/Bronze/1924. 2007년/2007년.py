correction = {
    1: 1,
    2: -2,
    3: 1,
    4: 0,
    5: 1,
    6: 0,
    7: 1,
    8: 1,
    9: 0,
    10: 1,
    11: 0,
    12: 1,
}

weekday = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

m, d = map(int, input().split())
d += sum(correction[i] + 30 for i in range(1, m))

print(weekday[d % 7])
