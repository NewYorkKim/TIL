import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while que:
        num = que.popleft()
        new = nums[num-1]

        if num not in visited:
            que.append(new)
            visited.append(num)

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    que = deque()
    visited = []

    cnt = 0

    for i in range(n):
        if i+1 not in visited:
            que.append(nums[i])
            visited.append(i+1)
            cnt += 1
            bfs()

    print(cnt)