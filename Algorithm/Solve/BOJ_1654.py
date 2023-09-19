k, n = map(int, input().split())
lengths =  [int(input()) for _ in range(k)]

start, end = 0, max(lengths)
result = 0

while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        mid = 1
    total = 0
    for length in lengths:
        total += length // mid
    if total < n:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)