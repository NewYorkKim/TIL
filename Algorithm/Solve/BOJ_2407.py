from math import comb

n, m = map(int, input().split())
result = comb(n, m)

print(result)