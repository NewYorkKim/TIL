n = int(input())
tips = sorted([int(input()) for _ in range(n)], reverse=True)

total = 0
for i in range(n):
    tip = tips[i] - i
    if tip <= 0:
        continue
    else:
        total += tip

print(total)