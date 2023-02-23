t = int(input())

for i in range(1, t+1):
    dirs = input()
    a, b = 1, 1
    for dir in dirs:
        if dir == 'L':
            b += a
        else:
            a += b
    print(f"#{i}", a, b)