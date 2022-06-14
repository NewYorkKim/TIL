# c = int(input())
# over_avg = []

# for i in range(c):
#     nums = list(map(int, input().split()))
#     avg = sum(nums[1:]) / nums[0]
#     cnt = 0
#     for i in range(1,len(nums)):
#         if nums[i] > avg:
#             cnt += 1
#     over = cnt / nums[0] * 100
#     over_avg.append(over)

# for j in over_avg:
#     print("%.3f%%"%(j))

c = int(input())

for i in range(c):
    students, *scores = map(int, input().split())
    avg = sum(scores) / students
    print(f'{sum(score > avg for score in scores) / students * 100:.3f}%')
