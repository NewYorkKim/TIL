t = int(input())

for i in range(1, t+1):
    k = int(input())
    nums = list(map(int, input().split()))
    tmp = nums.copy()

    total = 0
    while len(nums) > 1:
        for j in range(0, len(nums), 2):
            total += abs(nums[j] - nums[j+1])
            tmp.remove(min(nums[j], nums[j+1]))

        nums = tmp.copy()

    print(f"#{i}", total)
