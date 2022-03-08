# scores = []

# for i in range(5):
#     score = int(input())
#     if score < 40:
#         score = 40
#     scores.append(score)

# print(sum(scores) // 5)

scores = [max(40, int(input())) for i in range(5)]

print(sum(scores) // 5)