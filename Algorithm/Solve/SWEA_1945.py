t = int(input())

for i in range(1, t+1):
    n = int(input())
    num = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]
    for j in range(len(num)):
        if n == 1:
            break
        while n % num[j] == 0:
            n //= num[j]
            result[j] += 1
    print(f'#{i}', *result)

