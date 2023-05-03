t = int(input())

for i in range(t):
    n = int(input())
    fibo = [0] * (n + 2)
    fibo[0] = 0
    fibo[1] = 1
    for j in range(2, n+1):
        fibo[j] = fibo[j-1] + fibo[j-2]
    print(fibo[n-1], fibo[n])
