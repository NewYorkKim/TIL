from collections import deque
import sys
input = sys.stdin.readline

def bfs(que, sharks):
    dx = [0, 0, 1, -1, -1, 1, 1, -1]
    dy = [1, -1, 1, -1, 1, -1, 0, 0]

    while que:
        x, y = que.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if sharks[nx][ny] == 0:
                    sharks[nx][ny] = sharks[x][y] + 1
                    que.append((nx, ny))

n, m = map(int, input().split())
que = deque()
sharks = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            que.append((i, j))
    sharks.append(tmp)

bfs(que, sharks)

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, sharks[i][j])

print(result - 1)