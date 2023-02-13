t = int(input())

for i in range(1, t+1):
    nums = list(input().split())
    result = [0] * len(nums)

    for j in range(len(nums)):
        for x in nums[j]:
            result[j] += int(x)

    print(f"#{i}", max(result), min(result)) 
