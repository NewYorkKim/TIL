import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []

for i in range(n):
    x = list(map(int, input().split()))
    
    if x[0] == 0:
        if len(h) == 0:
            print(-1)
        else:
            print(-heapq.heappop(h))
    else:
        for j in range(x[0]):
            heapq.heappush(h, -x[j+1])