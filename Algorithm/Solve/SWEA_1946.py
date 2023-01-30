t = int(input())

for i in range(1, t+1):
    n = int(input())
    array = ''
    for _ in range(n):
        c, k = input().split()
        array += c*int(k)
    print(f'#{i}')
    for j in range(0, len(array), 10):
        print(''.join(array[j:j+10]))