t = int(input())

for i in range(t):
    array = list(map(int, input().split()))
    array = [x for x in array if x%2 != 0]
    print(f'#{str(i+1)}', sum(array))