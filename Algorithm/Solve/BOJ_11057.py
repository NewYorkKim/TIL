import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for k in range(10):
        tmp = 0
        for s in range(0, k+1):
            tmp += dp[i-1][s]
        dp[i][k] = tmp

result = 0
for i in range(10):
    result += dp[n][i]

print(result % 10007)
