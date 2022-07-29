n = int(input())

for i in range(n):
    a, b = input().split()
    print(''.join(j*int(a) for j in b))
        