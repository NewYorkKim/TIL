a = int(input())
seq = list(map(int, input().split()))

dp = [1] * a
ans = [seq[0]]

for i in range(1, a):
    tmp = 0
    for j in range(i+1):
        if seq[i] > seq[j]:
            tmp = max(tmp, max(seq[i-1] + seq[i], seq[i-1] + seq[j]))
    dp[i] = tmp
 
print(ans)
print(dp)