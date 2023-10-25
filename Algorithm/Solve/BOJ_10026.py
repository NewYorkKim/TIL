from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def bfs(u, v, color):
    que = deque()
    que.append((u, v))
    visited[u][v] = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n):
                if grid[nx][ny] == color and visited[nx][ny] == 0:
                    que.append((nx, ny))
                    visited[nx][ny] = 1

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

cnt1 = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            color = grid[i][j]
            bfs(i, j, color)
            cnt1 += 1

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == "G":
            grid[i][j] = "R"

cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            color = grid[i][j]
            bfs(i, j, color)
            cnt2 += 1

print(cnt1, cnt2)
