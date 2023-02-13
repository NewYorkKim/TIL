t = int(input())

for i in range(1, t+1):
    n = int(input())
    key = input()
    sc = input()

    cnt = 0
    for j in range(n):
        if key[j] == sc[j]:
            cnt += 1

    print(f"#{i}", cnt)