import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, r, visited, depth):
    global cnt
    visited[r] = True
    cnt += 1
    depth[r-1] = cnt
    
    graph[r] = sorted(graph[r])
    for i in graph[r]:
        if not visited[i]:
            dfs(graph, i, visited, depth)
    
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
depth = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
dfs(graph, r, visited, depth)

for j in depth:
    print(j)