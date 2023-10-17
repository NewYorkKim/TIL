from collections import deque
import sys
input = sys.stdin.readline

def bfs(graphs, visited, r):
    que = deque()
    que.append(r)
    cnt = 1
    visited[r] = cnt

    while que:
        r = que.popleft()

        for nr in graphs[r]:
            if visited[nr] == 0:
                cnt += 1
                visited[nr] = cnt
                que.append(nr)

    return visited

n, m, r = map(int, input().split())
graphs = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graphs[u].append(v)
    graphs[v].append(u)

for arr in graphs:
    arr.sort(reverse=True)

result = bfs(graphs, visited, r)[1:]

for i in result:
    print(i)