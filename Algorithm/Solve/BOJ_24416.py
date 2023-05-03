def dynamic_fibo(n, cnt, fibo):
    fibo[0] = fibo[1] = 1
    for i in range(2, n):
        fibo[i] = fibo[i-1] + fibo[i-2]
        cnt += 1
    return fibo[n-1], cnt

n = int(input())
fibo = [0] * n
cnt = 0

print(*dynamic_fibo(n, cnt, fibo))