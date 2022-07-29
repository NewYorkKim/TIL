n = int(input())

Chang_total = 100
Sang_total = 100

for i in range(n):
    Chang_dice, Sang_dice = map(int, input().split())
    if Chang_dice < Sang_dice:
        Chang_total -= Sang_dice
    elif Chang_dice > Sang_dice:
        Sang_total -= Chang_dice

print(Chang_total, Sang_total, sep='\n')