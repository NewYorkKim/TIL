import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

result = 0
while start <= end:
    mid = (start + end) // 2
    if mid < 1:
        mid = 1

    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)