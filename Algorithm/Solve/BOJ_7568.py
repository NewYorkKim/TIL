n = int(input())
array1 = []
dic = dict()

for i in range(n):
    x = tuple(map(int, input().split()))
    array1.append(x)
    dic[x] = 1

array2 = sorted(dic.keys(), reverse=True)

for i in range(len(array2)):
    for j in range(i+1):
        if (array2[i][0] < array2[j][0]) and (array2[i][1] < array2[j][1]):
            dic[array2[i]] += 1

for k in array1:
    print(dic[k], end=' ')


    
