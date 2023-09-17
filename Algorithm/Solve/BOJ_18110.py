import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    result = 0
else:
    cut = int(n * 0.15 + 0.5)
    levels = sorted([int(input()) for _ in range(n)])[cut: n-cut]

    result = int((sum(levels) / (n - (2 * cut))) + 0.5)

print(result)
