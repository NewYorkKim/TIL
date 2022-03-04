print('first array')
first = [list(map(int, input().split())) for i in range(2)]

print('second array')
second = [list(map(int, input().split())) for i in range(2)]

for j in range(2):
    print(*[x * y for x, y in zip(first[j], second[j])])