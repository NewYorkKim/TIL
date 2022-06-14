# lines = [input() for i in range(5)]
# lengths = [len(line) for line in lines]
# new = [list() for k in range(max(lengths))]

# for line in lines:
#     for j in range(len(line)):
#         new[j].append(line[j])

# for w in new:
#     print(''.join(w), end='')

result = ['' for i in range(75)]
for i in range(5):
    line = input()
    for j in range(len(line)):
        result[j * 5 + i] = line[j]

print(''.join(result))