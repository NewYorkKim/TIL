import sys
input = sys.stdin.readline

def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return 

    for i in range(1, n+1):
        ans.append(i)
        back()
        ans.pop()

n, m = map(int, input().split())
ans = []
tmp = []

back()