import sys
input = sys.stdin.readline

def back(idx):
    if len(tmp) == m:
        ans.add(tuple(tmp))
        return 

    for i in range(idx, n):
        tmp.append(nums[i])
        back(i)
        tmp.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []
ans = set()

back(0)

for i in sorted(list(ans)):
    print(" ".join(map(str, i)))