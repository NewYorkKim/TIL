from math import gcd

n = int(input())
trees = [int(input()) for i in range(n)]

gaps = [trees[i+1] - trees[i] for i in range(n-1)]
min_gap = gcd(gaps[0], gaps[1])

for i in range(1, n-1):
    min_gap = gcd(gaps[i], min_gap)

result = 0
for gap in gaps:
    result += gap // min_gap - 1

print(result)