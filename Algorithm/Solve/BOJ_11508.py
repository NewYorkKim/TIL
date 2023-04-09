n = int(input())
costs = sorted([int(input()) for _ in range(n)], reverse=True)
total = 0

for i in range(1, n+1):
    if i % 3 == 0:
        continue
    else:
        total += costs[i-1]

print(total)