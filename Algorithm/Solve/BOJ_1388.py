import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if floors[y][x] == "-":
        floors[y][x] = "0"
        for _x in [1, -1]:
            x = x + _x
            if (0 <= y < n) and (0 <= x < m):
                if floors[y][x] == "-":
                    dfs(x, y)

    if floors[y][x] == "|":
        floors[y][x] = "0"
        for _y in [1, -1]:
            y = y + _y
            if (0 <= y < n) and (0 <= x < m):
                if floors[y][x] == "|":
                    dfs(x, y)

n, m = map(int, input().split())
floors = [list(input().strip()) for _ in range(n)]
count = 0

for y in range(n):
    for x in range(m):
        if floors[y][x] == "-" or floors[y][x] == "|":
            dfs(x, y)
            count += 1

print(count)