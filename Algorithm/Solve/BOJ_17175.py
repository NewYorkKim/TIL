n = int(input())
fibo = [0] * (n+1)

for i in range(n+1):
    if (i == 0) or (i == 1):
        fibo[i] = 1
    else: 
        fibo[i] = (fibo[i-2] + fibo[i-1] + 1)

print(fibo[n] % 1000000007)