import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
o = []
cnt = 0

for i in range(n):
    x = int(input())
    heapq.heappush(h, -x)
    o.append(x)

while True:
    if (o[0] == max(o)) and (o.count(o[0]) == 1):
        print(cnt)
        break
    m1 = -heapq.heappop(h)
    m2 = m1 - 1
    heapq.heappush(h, -m2)
    if o[0] == m1:
        o.reverse()
        o[o.index(m1)] = m2
        o.reverse()
    else:
        o[o.index(m1)] = m2
    o[0] += 1
    cnt += 1