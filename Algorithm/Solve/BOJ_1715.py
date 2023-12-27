import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = []
ans = 0

for _ in range(n):
    heapq.heappush(cards, int(input()))

while len(cards) != 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    ans += tmp
    heapq.heappush(cards, tmp)

print(ans)