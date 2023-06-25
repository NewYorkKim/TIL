n = 1000000
a = [False, False] + [True] * n
primes = []

for i in range(2, n):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n, i):
            a[j] = False

t = int(input())

for _ in range(t):
    num = int(input())
    cnt = 0
    
    for j in range(2, num//2 + 1):
        if a[j] and a[num - j]:
            cnt += 1

    print(cnt)