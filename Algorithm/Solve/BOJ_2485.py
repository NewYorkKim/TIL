from math import gcd

n = int(input())
trees = [int(input()) for _ in range(n)]
gaps = []

for i in range(n-1):
    gaps.append(trees[i+1] - trees[i])

goal = max(gaps)

for j in range(len(gaps)-1):
    goal = min(gcd(gaps[j], gaps[j+1]), goal)

cnt = 0

for gap in gaps:
    cnt += gap//goal - 1

print(cnt)