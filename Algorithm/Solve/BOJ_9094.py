import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0

    for b in range(2, n):
        for a in range(1, b):
            result = (a**2 + b**2 + m) / (a * b)
            if result.is_integer():
                cnt += 1

    print(cnt)

