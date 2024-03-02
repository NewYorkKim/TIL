import sys
input = sys.stdin.readline

n = int(input())
points = [int(input()) for _ in range(n)][::-1]
idx, cnt = 1, 0

while idx < len(points):
    if points[idx-1] <= points[idx]:
        points[idx] -= 1
        cnt += 1
    else:
        idx += 1

print(cnt)
