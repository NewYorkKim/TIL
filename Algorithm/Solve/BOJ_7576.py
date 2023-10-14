from collections import deque
import sys
input = sys.stdin.readline

def bfs(que, tomatoes):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = tomatoes[x][y] + 1
                    que.append((nx, ny))

m, n = map(int, input().split())

que = deque()
tomatoes = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            que.append((i, j))
    tomatoes.append(tmp)

bfs(que, tomatoes)

result, flag = 0, False
for i in range(n):
    for j in range(m):
        result = max(result, tomatoes[i][j])
        
        if tomatoes[i][j] == 0:
            flag = True
            break

if flag:
    print(-1)
else:
    print(result - 1)
