N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

stack = [([], [False] * N)]
while stack:
    seq, used = stack.pop()
    if len(seq) == M:
        print(*seq)
        continue

    for n in range(N - 1, -1, -1):
        if not used[n]:
            new_seq = seq + [arr[n]]
            new_used = [x for x in used]
            new_used[n] = True
            stack.append((new_seq, new_used))
