# DFS & BFS

> 2022/07/25, 2022/11/04

- source: [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

`data structure` `algorithm` `python`



## DFS (Depth-First Search)

- **깊이 우선 탐색**이라고도 부르며 그래프에서 **깊은 부분을 우선적으로 탐색하는 알고리즘**
- **스택 자료구조 (혹은 재귀 함수)**를 이용
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함
    2. 스택의 최상단 노드에 방문하지 않고 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복



### Python 구현 예제

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visitied[i]:
            df(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
```

```python
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
```



## BFS (Breadth-First Search)

- **너비 우선 탐색**이라고도 부르며, 그래프에서 **가까운 노드부터 우선적으로 탐색하는 알고리즘**
- **큐 자료구조**를 이용
    1. 탐색 시작 노드를 큐에 삽입하여 방문 처리를 함
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 함
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복



### Python 구현 예제

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
```

```python
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
```