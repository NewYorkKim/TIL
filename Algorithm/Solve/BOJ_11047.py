n, k = map(int, input().split())
values = sorted([int(input()) for _ in range(n)], reverse=True)
cnt = 0

while k != 0:
    for value in values:
        if value <= k:
            cnt += k // value
            k %= value

print(cnt)
