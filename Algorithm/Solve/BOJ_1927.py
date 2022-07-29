import sys
import heapq

n = int(sys.stdin.readline())
h = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(h) > 0:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, x)