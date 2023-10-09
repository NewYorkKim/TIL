import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    global tmp
    tmp += 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < m) and (0 <= ny < n):
            if areas[ny][nx] == True:
                areas[ny][nx] = False
                dfs(nx, ny)

n, m, k = map(int, input().split())
spots = [list(map(int, input().split())) for _ in range(k)]
areas = [[False for _ in range(m)] for _ in range(n)]
result = 0

for spot in spots:
    x, y = spot[1] - 1, spot[0] - 1
    areas[y][x] = True

for y in range(n):
    for x in range(m):
        if areas[y][x] == True:
            tmp = 0
            areas[y][x] = False
            dfs(x, y)

            if tmp > result:
                result = tmp

print(result)