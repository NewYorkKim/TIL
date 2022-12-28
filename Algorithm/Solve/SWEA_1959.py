t = int(input())

for i in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = []
    for j in range(abs(n-m)+1):
        tmp = sum([a[k]*b[k+j] if n <= m else a[k+j]*b[k] for k in range(min(n, m))])
        result.append(tmp)
    print(f'#{i}', max(result))