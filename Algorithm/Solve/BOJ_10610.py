n = sorted(list(input()), reverse=True)
num = int(''.join(n))
answer = -1

if num % 30 == 0:
    answer = num
print(answer)