def dfs(graph, start, visited):
    global cnt
    visited[start] = True

    for i in range(len(graph[start])):
        if graph[start][i] and not visited[i]:
            cnt += 1
            dfs(graph, i, visited)


    return cnt

n = int(input())
m = int(input())

graph = [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

visited = [False] * (n+1)
cnt = 0

dfs(graph, 1, visited)
print(cnt)