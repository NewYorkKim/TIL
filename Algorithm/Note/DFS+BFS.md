# 트리

> 2022/07/25

- source: [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

`data structure` `algorithm` `python`



## DFS (Depth-First Search)

- **깊이 우선 탐색**이라고도 부르며 그래프에서 **깊은 부분을 우선적으로 탐색하는 알고리즘**
- **스택 자료구조 (혹은 재귀 함수)**를 이용
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함
    2. 스택의 최상단 노드에 방문하지 않고 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복



##### Python 구현 예제

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



## BFS (Breadth-First Search)

- **너비 우선 탐색**이라고도 부르며, 그래프에서 **가까운 노드부터 우선적으로 탐색하는 알고리즘**
- **큐 자료구조**를 이용
    1. 탐색 시작 노드를 큐에 삽입하여 방문 처리를 함
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 함
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복



##### Python 구현 예제

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