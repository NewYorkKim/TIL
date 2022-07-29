print('first array')
first= [map(int, input().split()) for i in range(2)]

print('second array')
second = [map(int, input().split()) for i in range(2)]

# print(*[i * j for i, j in zip(first[0], second[0])])
# print(*[k * l for k, l in zip(first[1], second[1])])

for k in range(2):
    print(*[i * j for i, j in zip(first[k], second[k])])