import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []

for i in range(n):
    x = int(input())
    if x == 0:
        if len(h) > 0:
            print(heapq.heappop(h)[1])
        else:
            print(0)
    else:
        heapq.heappush(h, (abs(x), x))