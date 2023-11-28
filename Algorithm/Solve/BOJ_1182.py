import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = []
cnt = 0

def back(idx):
    global cnt

    if (len(ans) > 0 and sum(ans) == s):
        cnt += 1
    
    for i in range(idx, n):
        ans.append(nums[i])
        back(i+1)
        ans.pop()

back(0)
print(cnt)