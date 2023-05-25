n, k = map(int, input().split())

cnt = 0
result = []

for i in range(1, n+1):
    if n % i != 0:
        continue
    result.append(i)
    cnt += 1

if len(result) < k:
    print(0)
else:
    print(result[k-1])