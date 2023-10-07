n = int(input())
cows = dict()
cnt = 0

for _ in range(n):
    num, pos = map(int, input().split())
    
    if num in cows:
        if cows[num] != pos:
            cnt += 1
            cows[num] = pos
    else:
        cows[num] = pos

print(cnt)
