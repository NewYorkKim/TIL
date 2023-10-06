from itertools import combinations

n = int(input())
tastes = [tuple(map(int, input().split())) for _ in range(n)]
diff = 1e9

for i in range(1, n+1):
    combs = combinations(tastes, i)
    for comb in combs:
        s = 1
        b = 0
        for taste in comb:
            s *= taste[0]
            b += taste[1]
        if diff > abs(s - b):
            diff = abs(s - b)

print(diff)


