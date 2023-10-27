from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    que = deque()
    que.append(1)
    visited[1] = True
    move[1] = 0
    
    while que:
        pos = que.popleft()

        for i in range(1, 7):
            next = pos + i

            if 1 <= next <= 100 and not visited[next]:
                if next in snake.keys():
                    next = snake[next]
                if next in ladder.keys():
                    next = ladder[next]
                if not visited[next]:
                    que.append(next)
                    visited[next] = True
                    move[next] = move[pos] + 1

n, m = map(int, input().split())

move = [0 for _ in range(101)]
visited = [False for _ in range(101)]

ladder = dict()
snake = dict()

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

bfs()
print(move[100])