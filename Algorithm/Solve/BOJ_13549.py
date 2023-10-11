from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, k):
    visited = [-1] * 100001
    que = deque()
    que.append(n)
    visited[n] = 0

    while que:
        pos = que.popleft()
        
        if pos == k:
            return visited[pos]
        
        if 0 <= pos-1 < 100001 and visited[pos-1] == -1:
            visited[pos-1] = visited[pos] + 1
            que.append(pos-1)
        if 0 <= pos*2 < 100001 and visited[pos*2] == -1:
            visited[pos*2] = visited[pos]
            que.appendleft(pos*2)
        if 0 <= pos+1 < 100001 and visited[pos+1] == -1:
            visited[pos+1] = visited[pos] + 1
            que.append(pos+1)
                    
n, k = map(int, input().split())
print(bfs(n, k))