from collections import deque
import sys
input = sys.stdin.readline

def bfs(graphs, start):
    counts = [0] * (n + 1)
    visited = [start]
    que = deque()
    que.append(start)

    while que:
        a = que.popleft()
        for i in graphs[a]:
            if i not in visited:
                counts[i] = counts[a] + 1
                visited.append(i)
                que.append(i)
    
    return sum(counts)

n, m = map(int, input().split())
graphs = [[] for _ in range(n + 1)]
result = []

for i in range(m):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

for i in range(1, n + 1):
    result.append(bfs(graphs, i))

print(result.index(min(result)) + 1)