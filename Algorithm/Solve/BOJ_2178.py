from collections import deque
import sys
input = sys.stdin.readline

def bfs(maze):
    visited = [[-1] * m for _ in range(n)]
    que = deque()
    que.append((0, 0))

    while que:
        x, y = que.popleft()

        if x == n - 1 and y == m - 1:
            return maze[n-1][m-1]
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] != 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = 0
                    maze[nx][ny] = maze[x][y] + 1
                    que.append((nx, ny))


n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

print(bfs(maze))