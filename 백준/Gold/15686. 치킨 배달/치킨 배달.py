import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken, house = [], []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

def get_distance(selected_indices):
    distance = 0
    for hx, hy in house:
        min_distance = float("inf")
        for idx in selected_indices:
            cx, cy = chicken[idx]
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        distance += min_distance
    return distance

stack = [(0, [])]
ans = float("inf")

while stack:
    start, select = stack.pop()
    if len(select) == m:
        ans = min(ans, get_distance(select))
        continue

    for i in range(len(chicken) - 1, start - 1, -1):
        if len(select) + (len(chicken) - i) < m:
            continue
        
        stack.append((i + 1, select + [i]))

print(ans)
