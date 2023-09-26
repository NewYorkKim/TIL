n, k = map(int, input().split())
max_n = 0

for i in range(1, k+1):
    tmp = int(str(n * i)[::-1])
    if tmp > max_n:
        max_n = tmp

print(max_n)