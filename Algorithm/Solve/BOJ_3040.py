from itertools import combinations

nums = [int(input()) for _ in range(9)]
combs = combinations(nums, 7)
result = []

for comb in combs:
    if sum(comb) == 100:
        result = list(comb)
        break

for i in result:
    print(i)