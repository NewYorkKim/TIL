t = int(input())

for i in range(1, t+1):
    n = int(input())
    array = list(map(int, input().split()))
    dic = dict()
    for j in array:
        if abs(j) in dic.keys():
            dic[abs(j)] += 1
        else:
            dic[abs(j)] = 1
    result = sorted(dic.items(), key=lambda x: x[0])[0]
    print(f'#{i}', *(result))