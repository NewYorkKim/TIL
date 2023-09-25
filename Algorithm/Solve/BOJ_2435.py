n, k = map(int, input().split())
nums = list(map(int, input().split()))
result = -1e9

for i in range(len(nums)-k+1):
    tmp = sum(nums[i:i+k])
    if tmp > result:
        result = tmp

print(result)