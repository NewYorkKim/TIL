import sys
input = sys.stdin.readline

def back():
    if len(tmp) == m:
        ans.add(tuple(tmp))
        return 

    for i in range(n):
        tmp.append(nums[i])
        back()
        tmp.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []
ans = set()

back()

for i in sorted(list(ans)):
    print(" ".join(map(str, i)))