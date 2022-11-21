t = int(input())

for i in range(t):
    array = list(map(int, input().split()))
    print(f'#{str(i+1)}', max(array))