t = int(input())

for i in range(1, t+1):
    n = int(input())
    array = list(map(int, input().split()))
    dic = dict()
    for j in array:
        if j in dic.keys():
            dic[j] += 1
        else:
            dic[j] = 1
    mode = sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0]
    print(f'#{i}', mode)