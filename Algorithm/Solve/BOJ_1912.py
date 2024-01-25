import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n+1):
    if i == 1:
        dp[i] = nums[i-1]
    else:
        dp[i] = max(dp[i-1] + nums[i-1], nums[i-1])

print(max(dp[1:]))