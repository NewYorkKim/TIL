from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, k):
    que = deque()
    que.append(n)
    way = [0] * 100001
    total, cnt = 0, 0

    while que:
        pos = que.popleft()
        tmp = way[pos]

        if pos == k:
            cnt = tmp
            total += 1
            continue

        for np in [pos-1, pos+1, pos*2]:
            if 0 <= np < 100001 and (way[np] == 0 or way[np] == way[pos] + 1):
                way[np] = way[pos] + 1
                que.append(np)

    return total, cnt

n, k = map(int, input().split())

total, cnt = bfs(n, k)

print(cnt)
print(total)
