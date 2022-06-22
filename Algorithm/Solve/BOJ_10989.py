import sys
input = sys.stdin.readline

n = int(input())
cnt = [0] * 10001

for i in range(n):
    x = int(input())
    cnt[x] += 1

for i in range(10001):
    for j in range(cnt[i]):
        print(i)