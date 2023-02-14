n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]
rank = [1] * n

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if (array[i][0] > array[i][0]) and (array[i][1] > array[j][1]):
            continue
        elif (array[i][0] < array[j][0]) and (array[i][1] < array[j][1]):
            rank[i] += 1

print(*rank)
