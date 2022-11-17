t = int(input())
time = [300, 60, 10]
cnt = [0, 0, 0]

while t != 0:
    if t < 10:
        cnt = [-1]
        break
    for i in range(3):
        if t >= time[i]:
            cnt[i] += t // time[i]
            t %= time[i]

print(*cnt)