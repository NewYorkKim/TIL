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

        if (0 <= nx < n) and (0 <= ny < n):
            if apts[ny][nx] == 1:
                apts[ny][nx] = 0
                dfs(nx, ny)

n = int(input())
apts = [list(map(int, input().strip())) for _ in range(n)]
counts = []

for x in range(n):
    for y in range(n):
        if apts[y][x] == 1:
            apts[y][x] = 0
            tmp = 0
            dfs(x, y)
            counts.append(tmp)

print(len(counts))

counts.sort()
for count in counts:
    print(count)