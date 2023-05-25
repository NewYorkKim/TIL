a = int(input())
seq = list(map(int, input().split()))

dp = [1] * a
ans = [seq[0]]

for i in range(1, a):
    for j in range(i+1):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j]+1)
 
print(ans)