# n = int(input())

# seq = list(map(int, input().split()))
# result = []

# for i in range(n):
#     if seq[i] > 0:
#         result.insert(-(seq[i]), i + 1)
#     else:
#         result.append(i + 1)

# print(*result)

n = int(input())

seq = list(map(int, input().split()))
result = []

for i in range(n):
    result.insert(i - seq[i], i + 1)

print(*result)