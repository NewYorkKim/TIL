t = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in range(1, t+1):
    n = int(input())
    change = []
    for m in money:
        if n >= m:
            change.append(n//m)
            n %= m
        else:
            change.append(0)
    print(f'#{i}')
    print(*change)