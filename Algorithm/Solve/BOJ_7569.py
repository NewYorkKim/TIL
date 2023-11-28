import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graphs = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[False] * m for i in range(n * h)]

que = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graphs[i][j][k] == 1:
                que.append((i, j, k))

while que:
    z, x, y = que.popleft()
    
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if graphs[nz][nx][ny] == 0:
                graphs[nz][nx][ny] = graphs[z][x][y] + 1
                que.append((nz, nx, ny))

day = 0
flag = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graphs[i][j][k] == 0:
                flag = True
                break
            day = max(day, graphs[i][j][k])

if flag:
    print(-1)
else:
    print(day-1)