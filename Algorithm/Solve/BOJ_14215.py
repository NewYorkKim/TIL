sides = sorted(list(map(int, input().split())))
a, b, c = sides[0], sides[1], sides[2]

if c < a + b:
    print(a + b + c)
else:
    c = a + b - 1
    print(a + b + c)