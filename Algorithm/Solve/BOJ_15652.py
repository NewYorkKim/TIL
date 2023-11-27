import sys
input = sys.stdin.readline

def back(idx):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return 
    
    for i in range(idx, n+1):
        ans.append(i)
        back(i)
        ans.pop()

n, m = map(int, input().split())
ans = []

back(1)