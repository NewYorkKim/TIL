t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    if a < b:
        result = '<'
    elif a == b:
        result = '='
    else:
        result = '>'

    print(f'#{str(i+1)}', result)