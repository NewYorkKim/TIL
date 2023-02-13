import math

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())

    cnt = 0
    for j in range(a, b+1):
        if str(j) == str(j)[::-1]:
            sqr = str(math.sqrt(j))
            idx = sqr.index('.')
            if sqr[idx+1:] =='0':
                sqr = sqr[:idx]
            if sqr == sqr[::-1]:
                cnt += 1

    print(f"#{i}", cnt)