a = int(input())
sequence = list(map(int, input().split()))

dp = [1] * a
ans = [1]

for i in range(1, a):
    for j in range(i+1):
        if sequence[i] < sequence[j]:
            dp[i] = max(dp[i], dp[j]+1)
    if dp[i] == dp[i-1]:
        ans.pop()
        ans.append(sequence[i])
    else:
        ans.append(sequence[i])

print(sum(ans))

