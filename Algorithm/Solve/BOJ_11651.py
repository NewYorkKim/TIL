import sys
input = sys.stdin.readline

n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]
array = sorted(array, key=lambda x: (x[1], x[0]))

for nums in array:
    print(nums[0], nums[1])