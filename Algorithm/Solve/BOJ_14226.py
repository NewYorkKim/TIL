from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    que = deque()
    que.append((1, 0))
    visited = dict()
    visited[(1, 0)] = 0

    while que:
        emo, clip = que.popleft()

        if emo == s:
            return visited[(emo, clip)]
        
        if (emo, emo) not in visited.keys():
            visited[(emo, emo)] = visited[(emo, clip)] + 1
            que.append((emo, emo))
        if (emo + clip, clip) not in visited.keys():
            visited[(emo + clip, clip)] = visited[(emo, clip)] + 1
            que.append((emo + clip, clip))
        if (emo - 1, clip) not in visited.keys():
            visited[(emo - 1, clip)] = visited[(emo, clip)] + 1
            que.append((emo - 1, clip))

s = int(input())

print(bfs(s))