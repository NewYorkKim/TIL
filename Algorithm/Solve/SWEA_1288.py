t = int(input())

for i in range(1, t+1):
    n = int(input())
    numbers = set()
    cnt = 1
    while len(numbers) != 10:
            target = n * cnt
            numbers.update(str(target))
            cnt += 1
    print(f'#{i}', target)
        