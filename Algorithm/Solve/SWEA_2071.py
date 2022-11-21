t = int(input())

for i in range(t):
    array = list(map(int, input().split()))
    avg = sum(array) / 10
    print(f'#{str(i+1)}', round(avg))