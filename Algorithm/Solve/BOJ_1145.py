from itertools import combinations
from math import lcm

nums = list(map(int, input().split()))
combs = combinations(nums, 3)
result = 1e9

for comb in combs:
    tmp = lcm(comb[0], comb[1], comb[2])
    if tmp < result:
        result = tmp

print(result)

