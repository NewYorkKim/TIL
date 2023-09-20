n,c = map(int, input().split())
homes = sorted([int(input()) for _ in range(n)])

start, end = 1, (homes[-1] - homes[0])
while start <= end:
    mid = (start + end) // 2
    count = 1
    previous = homes[0]

    for home in homes:
        if home - previous >= mid:
            previous = home
            count += 1
    
    if count >= c:
        start = mid + 1

    else:
        end = mid - 1

print(end)
    