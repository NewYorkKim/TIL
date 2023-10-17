from collections import deque
import sys
input = sys.stdin.readline

def bfs(x1, y1, x2, y2):
    que = deque()
    que.append((x1, y1))

    while que:
        x, y = que.popleft()

        if (x == x2) and (y == y2):
            return visited[x][y] - 1

        dx = [-2, -2, -1, -1, 1, 1, 2, 2]
        dy = [-1, 1, -2, 2, -2, 2, -1, 1]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < l) and (0 <= ny < l):
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))

t = int(input())

for _ in range(t):
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2= map(int, input().split())

    visited[x1][y1] = 1

    print(bfs(x1, y1, x2, y2))