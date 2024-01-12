from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    que = deque()
    que.append((0, 0))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while que:
        x, y  = que.popleft()
        visited[x][y] = 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    que.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
                    
    if visited[n-1][m-1]:
        answer = maps[n-1][m-1]
        return answer
    else:
        return -1