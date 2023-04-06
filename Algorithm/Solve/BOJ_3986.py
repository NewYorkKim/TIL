n = int(input())
cnt = 0

for i in range(n):
    string = list(input())
    tmp = []

    for j in string:
        if (len(tmp) == 0) or (tmp[-1] != j):
            tmp.append(j)
        else:
            tmp.pop()
    
    if len(tmp) == 0:
        cnt += 1

print(cnt)
