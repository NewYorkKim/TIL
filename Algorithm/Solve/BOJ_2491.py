n = int(input())
num = list(map(int, input().split()))

ans1 = [1] * n
ans2 = [1] * n

for i in range(1, n):
    if num[i] >= num[i - 1]:
        ans1[i] = max(ans1[i], ans1[i - 1] + 1)
    if num[i] <= num[i - 1]:
        ans2[i] = max(ans2[i], ans2[i - 1] + 1)

print(max(max(ans1), max(ans2)))