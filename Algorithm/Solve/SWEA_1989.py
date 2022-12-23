t = int(input())

for i in range(1, t+1):
    word = input()
    if word == word[::-1]:
        result = 1
    else:
        result = 0
    print(f'#{i}', result)