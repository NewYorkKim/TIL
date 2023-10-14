import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(graph, visited, r):
    global cnt

    visited[r] = cnt
    cnt += 1
    
    for v in graph[r]:
        if visited[v] == 0:
            dfs(graph, visited, v)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n + 1):
    graph[i].sort(reverse=True)

cnt = 1
dfs(graph, visited, r)

for i in visited[1:]:
    print(i)
