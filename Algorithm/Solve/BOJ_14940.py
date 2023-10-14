from collections import deque
import sys
input = sys.stdin.readline

def bfs(que, land, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if land[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
    
    return visited

n, m = map(int, input().split())
visited = [[-1] * m for _ in range(n)]
que = deque()
land = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            visited[i][j] = 0
            que.append((i, j))
        elif tmp[j] == 0:
            visited[i][j] = 0
    land.append(tmp)

result = bfs(que, land, visited)

for i in range(n):
        print(*result[i])