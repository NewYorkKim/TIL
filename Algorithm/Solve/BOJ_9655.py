import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n+1):
    if i <= 2:
        dp[i] = i
    else:
        dp[i] = min(dp[i-1]+1, dp[i-3]+1)

if dp[n] % 2 != 0:
    print("SK")
else:
    print("CY")