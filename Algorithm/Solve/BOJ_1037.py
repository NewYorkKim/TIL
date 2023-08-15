n = int(input())
nums = list(map(int, input().split()))

result = min(nums) * max(nums)
print(result)