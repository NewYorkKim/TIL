s = input()
cnt1, cnt2 = 0, 0

for i in s.split('0'):
    if i != '':
        cnt1 += 1

for j in s.split('1'):
    if j != '':
        cnt2 += 1

print(min(cnt1, cnt2))
