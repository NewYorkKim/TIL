nums = [num**2 for num in list(map(int, input().split()))]

print(sum(nums) % 10)