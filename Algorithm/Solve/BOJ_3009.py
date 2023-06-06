x, y = [], []

for i in range(3):
    a, b = map(int, input().split())

    x.append(a)
    if x.count(a) == 2:
        x.remove(a)
        x.remove(a)

    y.append(b)
    if y.count(b) == 2:
        y.remove(b)
        y.remove(b)

print(x[0], y[0])