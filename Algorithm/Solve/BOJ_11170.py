t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0

    for i in range(n, m+1):
        word = str(i)
        cnt += word.count("0")

    print(cnt)

