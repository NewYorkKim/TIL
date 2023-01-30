from datetime import datetime

t = int(input())

for i in range(1, t+1):
    m1, d1, m2, d2 = input().split()
    date1 = datetime.strptime(m1+d1, '%m%d')
    date2 = datetime.strptime(m2+d2, '%m%d')
    diff = date2 - date1
    print(f'#{i}', diff.days+1)
