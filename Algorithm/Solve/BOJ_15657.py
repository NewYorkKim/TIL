import sys
input = sys.stdin.readline

def back(idx):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return 
    
    for i in range(idx, n):
        ans.append(nums[i])
        back(i)
        ans.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []

back(0)