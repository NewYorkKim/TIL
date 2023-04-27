import math

n = int(input())
n_fac = str(math.factorial(n))[::-1]
cnt = 0

for i in n_fac:
    if i != '0':
        break
    else:
        cnt += 1

print(cnt)
