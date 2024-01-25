import sys
input = sys.stdin.readline

n, k = map(int, input().split())
res = [list(map(int, input().split())) for _ in range(n)]
res.sort(key=lambda x: (-x[1], -x[2], -x[3]))

grade, tmp = 1, 0
for i in range(n):
    if i != 0:
        if res[i][1:] == res[i-1][1:]:
            tmp += 1
        else:
            if tmp:
                grade += tmp
                tmp = 0
            grade += 1
    if res[i][0] == k:
        print(grade)
        break