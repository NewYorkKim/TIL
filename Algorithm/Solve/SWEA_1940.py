t = int(input())

for i in range(1, t+1):
    n = int(input())
    distance = 0
    speed = 0
    for j in range(n):
        c = list(map(int, input().split()))
        if len(c) == 1:
            distance += speed
        else:
            if c[0] == 1:
                speed += c[1]
                distance += speed
            else:
                speed -= c[1]
                if speed < 0:
                    speed = 0
                distance += speed
    print(f'#{i}', distance)

