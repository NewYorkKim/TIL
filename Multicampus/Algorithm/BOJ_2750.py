# n = int(input())

# nums = [int(input()) for i in range(n)]
# nums.sort()

# for num in nums:
#     print(num)

n = int(input())

nums = [int(input()) for i in range(n)]

for num in sorted(nums):
    print(num)
