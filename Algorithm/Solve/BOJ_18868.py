m, n = map(int, input().split())
spaces = [list(map(int, input().split())) for _ in range(m)]
sizes = []

for space in spaces:
    tmp = ""
    for i in range(n-1):
        for j in range(i+1, n):
            if space[i] > space[j]:
                tmp += "+"
            elif space[i] == space[j]:
                tmp += "="
            else:
                tmp += "-"
    sizes.append(tmp)

cnt = 0
for i in range(m-1):
    for j in range(i+1, m):
        if sizes[i] == sizes[j]:
            cnt += 1

print(cnt)