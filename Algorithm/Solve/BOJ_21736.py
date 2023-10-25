from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c):
    global cnt
    que = deque()
    que.append((r, c))
    visited[r][c] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if campus[nx][ny] != "X" and visited[nx][ny] == False:
                    if campus[nx][ny] == "P":
                        cnt += 1
                        que.append((nx, ny))
                        visited[nx][ny] = True
                    elif campus[nx][ny] == "O":
                        que.append((nx, ny))
                        visited[nx][ny] = True

n, m = map(int, input().split())
campus = []
visited = [[False] * m for _ in range(n)]
x, y = 0, 0
cnt = 0

x, y = 0, 0
for i in range(n):
    rows = list(input().strip())
    campus.append(rows)

    for j in range(m):
        if rows[j] == "I":
            x, y = i, j

bfs(x, y)

if cnt == 0:
    print("TT")
else:
    print(cnt)


