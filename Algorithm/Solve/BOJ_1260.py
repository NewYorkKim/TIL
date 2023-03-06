from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for j in range(len(graph[v])):
        if graph[v][j] and not visited[j]:
            dfs(graph, j, visited)

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    while queue:
        value = queue.popleft()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True
            for j in range(len(graph[v])):
                if graph[value][j] and not visited[j]:
                    queue.append(j)

n, m, v = map(int, input().split())
graph = [[False]*(n+1) for _ in range(n+1)]
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

dfs(graph, v, visited1)
print('\n', end='')
bfs(graph, v, visited2)
