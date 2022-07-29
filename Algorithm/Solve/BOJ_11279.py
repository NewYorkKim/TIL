import sys
import heapq

n = int(sys.stdin.readline())
h = []

for i in range(n):
    x = int(sys.stdin.readline())
    heapq.heappush(h, -x)

    if x == 0:
        print(-heapq.heappop(h))