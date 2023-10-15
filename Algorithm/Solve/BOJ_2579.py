import sys
input = sys.stdin.readline

n = int(input())
steps = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)
dp[1] = steps[1]

for i in range(2, n + 1):
    dp[i] = max(steps[i] + dp[i-2], steps[i] + steps[i-1] + dp[i-3])

print(dp[n])
