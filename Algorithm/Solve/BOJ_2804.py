a, b = input().split()

for i in range(len(a)):
    if a[i] in b:
        col = i
        row = b.index(a[i])
        break

for i in range(len(b)):
    if i == row:
        print(a)
    else:
        print('.'*col + b[i] + '.'*(len(a) - col - 1))


