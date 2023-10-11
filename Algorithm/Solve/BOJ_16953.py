from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    que = deque()
    que.append((a, 1))

    while que:
        a, cnt = que.popleft()

        if a == b:
            return cnt
        
        a1 = a * 2
        a2 = a * 10 + 1

        if a1 <= b:
            que.append((a1, cnt+1))
        if a2 <= b:
            que.append((a2, cnt+1))
    
    return -1

a, b = map(int, input().split())

print(bfs(a, b))