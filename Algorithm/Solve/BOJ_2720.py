t = int(input())
changes = [25, 10, 5, 1]

for _ in range(t):
    money = int(input())
    cnt = [0, 0, 0, 0]
    for i in range(len(changes)):
        if money == 0:
            break
        cnt[i] = money // changes[i]
        money %= changes[i]
    print(*cnt)