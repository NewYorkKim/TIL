from itertools import combinations

n, m = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(n)]
nums = list(range(m))
combs = combinations(nums, 3)
result = 0

for comb in combs:
    tmp = 0
    for i in range(n):
        score = scores[i]
        tmp += max(score[comb[0]], score[comb[1]], score[comb[2]])
    if tmp > result:
        result = tmp

print(result)
