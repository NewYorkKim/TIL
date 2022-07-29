n = int(input())

for i in range(n):
    sentence = input().split()
    result = [word[::-1] for word in sentence]
    print(*result)