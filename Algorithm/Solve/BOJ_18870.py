import sys
input = sys.stdin.readline

n = int(input())
xs = list(map(int, input().split()))
xs_sorted = sorted(set(xs))

idx = {}

for i in range(len(xs_sorted)):
    idx[xs_sorted[i]] = i

for j in range(n):
    print(idx[xs[j]], end=" ")