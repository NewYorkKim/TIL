import sys
input = sys.stdin.readline

def back(idx):
    if len(ans) == m:
        print(" ".join(map(str, ans)))

    for i in range(idx+1, n+1):
        if i not in ans:
            ans.append(i)
            back(i)
            ans.pop()

    return 

n, m = map(int, input().split())
ans = []

back(0)