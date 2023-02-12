t = int(input())

for i in range(1, t+1):
    n = int(input())
    income = sorted(list(map(int, input().split())))
    avg = sum(income) / len(income)
    
    cnt = 0
    for j in income:
        if j <= avg:
            cnt += 1
        else:
            break
    
    print(f"#{i}", cnt)
