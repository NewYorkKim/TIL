import sys
input = sys.stdin.readline

def back(idx):
    if len(tmp) == m:
        ans.add(tuple(tmp))
        return 
    
    for i in range(n):
        if check[i] is not True:
            tmp.append(nums[i])
            check[i] = True
            back(i)
            tmp.pop()
            check[i] = False
    

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
check = [False] * (n + 1)
tmp = []
ans = set()

back(0)

for i in sorted(list(ans)):
    print(" ".join(map(str, i)))