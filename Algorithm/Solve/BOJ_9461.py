t = int(input())

for _ in range(t):
    n = int(input())
    p = [1, 1, 1, 2, 2] + [0] * (n - 5)

    if n < 5:
        print(p[n-1])
    else:
        for i in range(5, n):
            p[i] = p[i-2] + p[i-3]
        print(p[n-1])
