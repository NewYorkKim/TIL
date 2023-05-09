a = int(input())
sequence = list(map(int, input().split()))
dp = [1] * (a+1)

for i in range(1, a):
    for j in range(0, i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
