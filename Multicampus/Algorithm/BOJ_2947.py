# seq = list(map(int, input().split()))

# for i in range(len(seq) - 1):
#     for j in range(1, len(seq)):
#         temp = 0
#         if seq[j - 1] > seq[j]:
#             temp = seq[j - 1]
#             seq[j - 1] = seq[j]
#             seq[j] = temp
#             print(' '.join(str(k) for k in seq))

seq = input().split()

for i in range(len(seq)):
    for j in range(len(seq) - 1):
        if seq[j] > seq[j + 1]:
            seq[j], seq[j + 1] = seq[j + 1], seq[j]
            print(*seq)