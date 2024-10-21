score = [0, 0]
time = [0, 0]
previous_time = 0
for _ in range(int(input())):
    inp = input().split()
    h, m = map(int, inp[1].split(":"))

    if score[0] != score[1]:
        time[score.index(max(score))] += h * 60 + m - previous_time

    previous_time = h * 60 + m
    score[int(inp[0]) - 1] += 1

if score[0] != score[1]:
    time[score.index(max(score))] += 48 * 60 - previous_time

print(f"{time[0]//60:02}:{time[0]%60:02}")
print(f"{time[1]//60:02}:{time[1]%60:02}")
