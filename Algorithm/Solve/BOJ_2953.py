# rank = 0
# total = 0

# for i in range(5):
#     score = list(map(int, input().split()))
#     if sum(score) > total:
#         total = sum(score)
#         rank = i + 1

# print(rank, total)

total = [sum(map(int, input().split())) for i in range(5)]
first = max(total)

print(total.index(first) + 1, first)