import sys
input = sys.stdin.readline

def check(n, types):
    ans = 1e9

    if n > 32:
        print(0)
        
    else:
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    tmp = 0
                    for x in range(4):
                        if types[i][x] != types[j][x]:
                            tmp += 1
                        if types[j][x] != types[k][x]:
                            tmp += 1
                        if types[i][x] != types[k][x]:
                            tmp += 1
                    ans = min(tmp, ans)
        print(ans)

t = int(input())

for _ in range(t):
    n = int(input())
    types = input().split()

    check(n, types)