from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

total = [sum(comb) for comb in combinations(cards, 3) if sum(comb) <= m]
total = sorted(total, key=lambda x: abs(m-x))

print(total[0])
