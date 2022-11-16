from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    print(count_by_range(cards, num, num), end=' ')