n = int(input())
array = sorted(list(map(int, input().split())))
idx = (n - 1) // 2
print(array[idx])