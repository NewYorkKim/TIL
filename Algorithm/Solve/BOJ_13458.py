import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = n

for i in a:
    i -= b
    if i > 0:
        cnt += math.ceil(i/c)

print(cnt)