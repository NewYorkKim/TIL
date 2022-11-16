def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
        

n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    print(binary_search(array, num, 0, n-1))