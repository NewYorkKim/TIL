background = [0] * 10000

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            background[j * 100 + k] = 1

print(sum(background))