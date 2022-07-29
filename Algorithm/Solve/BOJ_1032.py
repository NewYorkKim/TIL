# n = int(input())

# lines = [input() for i in range(n)]
# line = list(lines[0])

# for j in range(len(line)):
#     for k in range(len(lines) - 1):
#         if lines[k][j] != lines[k + 1][j]:
#             line[j] = '?'

# print(''.join(line))

n = int(input())
line = list(input())

for i in range(n - 1):
    other = input()
    for j in range(len(line)):
        if line[j] != other[j]:
            line[j] = '?'

print(''.join(line))