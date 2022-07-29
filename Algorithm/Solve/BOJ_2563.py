# background = [[0 for i in range(100)] for j in range(100)]

# n = int(input())

# for i in range(n):
#     x, y = map(int, input().split())
#     for j in range(10):
#         for k in range(10):
#             background[x-1+j][y-1+k] = 1

# print(sum(map(sum, background)))

background = [0] * 10000

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x + 10):
        for k in range(y + 10):
            background[j * 100 + k] = 1

print(sum(background))
