def dfs(v, e):
    parity = [0] * (v+1)

    for start in range(1,v+1):

        if parity[start]:
            continue

        stack = [(start, 1)]
        parity[start] = 1

        while stack:
            node, p = stack.pop()

            for nxt in graph[node]:
                if parity[nxt]==p:
                    return False
                
                if parity[nxt]==0:
                    stack.append((nxt, -p))
                    parity[nxt] = -p

    return True




import sys

input = sys.stdin.readline

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print("YES" if dfs(v, e) else "NO")