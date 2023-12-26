import sys
input = sys.stdin.readline

def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return 
    
    for i in range(n):
        if nums[i] not in ans:
            ans.append(nums[i])
            back()
            ans.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []

back()