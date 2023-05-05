import sys
input = sys.stdin.readline

mod = 1000000000
n = int(input())
fibo = [0, 1]

if abs(n) >= 1:
    for i in range(2, abs(n) + 1):
        fibo.append((fibo[i-1] + fibo[i-2]) % mod)
    print(-1 if (n < 0) and (n % 2 == 0) else 1, fibo[abs(n)], sep='\n')
else:
    print(n, abs(n), sep='\n')