n, m = map(int, input().split())
basket = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp = basket[i-1:j][::-1]

    for k in range(j-i+1):
        basket[i-1+k] = tmp[k]

print(*basket)