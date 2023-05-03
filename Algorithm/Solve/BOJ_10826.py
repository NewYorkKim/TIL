n = int(input())
fibo = [0] * (n + 1)

for i in range(n+1):
    if i == 0:
        fibo[i] = 0
    elif i == 1:
        fibo[i] = 1
    else:
        fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[n])