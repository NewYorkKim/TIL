import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
grounds = sum([list(map(int, input().split())) for _ in range(n)], [])
start, end = min(grounds), max(grounds)
result, height = 1e9, -1

for i in range(start, end+1):
    inven = b
    cnt = 0
    for ground in grounds:
        if ground > i:
            diff = ground - i
            cnt += diff * 2
            inven += diff
        else:
            diff = i - ground
            cnt += diff
            inven -= diff

    if (inven >= 0) and (cnt <= result):
        result = cnt
        height = i
    
print(result, height)