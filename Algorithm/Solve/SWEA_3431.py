t = int(input())

for i in range(1, t+1):
    l, u, x = map(int, input().split())
    if x >= l:
        if x <= u:
            result = 0
        else:
            result = -1
    else:
        result = l-x
    print(f"#{i}", result)