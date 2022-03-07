n = int(input())
k = 2

while n > 1:
    if n % k == 0:
        print(k)
        n /= k
    else:
        k += 1