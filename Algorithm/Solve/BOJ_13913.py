from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, k):
    visited = [-1] * 100001
    que = deque()
    que.append(n)
    visited[n] = n

    while que:
        pos = que.popleft()

        if pos == k:
            path = []
            while pos != n:
                path.append(pos)
                pos = visited[pos]
            path.append(n)

            return path
        
        for np in (pos - 1, pos + 1, pos * 2):
            if 0 <= np < 100001 and visited[np] == -1:
                visited[np] = pos
                que.append(np)

n, k = map(int, input().split())
result = bfs(n, k)

print(len(result) - 1)
print(*result[::-1])