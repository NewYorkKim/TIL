a, b = map(int, input().split())
b2 = b + 1
if b2 > 3:
    b2 %= 3

if a == b2:
    print('A')
else:
    print('B')