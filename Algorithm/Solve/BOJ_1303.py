import sys
sys.setrecursionlimit(10000)

def dfs(x, y, type):
    global tmp
    tmp += 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if men[ny][nx] == type:
                men[ny][nx] = "0"
                dfs(nx, ny, type)

n, m = map(int, input().split())
men = [list(input().strip()) for _ in range(m)]
countW, countB = 0, 0

for y in range(m):
    for x in range(n):
        if men[y][x] != "0":
            tmp = 0
            type = men[y][x]
            men[y][x] = " "
            dfs(x, y, type)

            if type == "W":
                countW += tmp ** 2
            else:
                countB += tmp ** 2

print(countW, countB)