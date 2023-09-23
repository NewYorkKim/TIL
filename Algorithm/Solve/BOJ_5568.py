from itertools import permutations

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]

result = set()
combs = list(permutations(cards, k))

for comb in combs:
    new = "".join(map(str, comb))

    result.add(new)

print(len(result))