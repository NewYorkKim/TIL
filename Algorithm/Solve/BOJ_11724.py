import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, v, visited):
    global tmp
    visited[v] = True
    tmp.append(v)

    for i in range(len(graph[v])):
        if graph[v][i] and not visited[i]:
            visited[v] = True
            dfs(graph, i, visited)

n, m = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

tmp = []
cnt = 0
for i in range(1, n+1):
    if len(tmp) == n:
        break
    if i not in tmp:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)