from itertools import permutations

n = int(input())
nums = range(1, n + 1)
pers = permutations(nums, n)

for per in pers:
    print(*per)