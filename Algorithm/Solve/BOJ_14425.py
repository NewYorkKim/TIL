n, m = map(int, input().split())
vocas = set(input() for _ in range(n))
cnt = 0

for _ in range(m):
    voca = input()

    if voca in vocas:
        cnt += 1

print(cnt)