n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

ans = []

for i in range(n):
    tmp = []
    for j in range(m):
        print(a[i][j] + b[i][j], end=" ")
    print()