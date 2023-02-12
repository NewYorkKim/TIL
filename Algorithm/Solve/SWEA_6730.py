t = int(input())

for i in range(1, t+1):
    n = int(input())
    blocks = list(map(int, input().split()))

    up, down = 0, 0

    for i in range(1, n):
        diff = blocks[i-1] - blocks[i]
        if (diff > 0) and (diff > down):
            down = diff
        elif (diff < 0) and (-diff > up):
            up = -diff

    print(f"#{i}", up, down)
