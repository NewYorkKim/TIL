from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    items = dict(Counter([input().split()[1] for _ in range(n)]))

    result = 1 
    for value in items.values():
        result *= (value + 1)

    print(result - 1)