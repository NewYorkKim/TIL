import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    que = deque()

    for i in graph[p1]:
        que.append((p1, i, 1))
        visited.append(p1)

        while que:
            x, y, cnt = que.popleft()

            if y == p2:
                return cnt
            
            for j in graph[y]:
                if j not in visited:
                    que.append((y, j, cnt+1))
                    visited.append(y)

    return -1

n = int(input())
p1, p2 = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = []

m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs())
