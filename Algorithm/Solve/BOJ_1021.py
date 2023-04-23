from collections import deque

n, m = map(int, input().split())
idxes = list(map(int, input().split()))
cards = deque([i+1 for i in range(n)])