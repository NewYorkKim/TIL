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
        
        for np in (pos + 1, pos - 1, pos * 2):
            if 0 <= np < 100001 and visited[np] == -1:
                visited[np] = visited[pos] + 1
                que.append(np)

n, k = map(int, input().split())
print(bfs(n, k))