a, b = map(int, input().split())
a_nums = set(map(int, input().split()))
b_nums = set(map(int, input().split()))

a_sub_b = a_nums - b_nums
b_sub_a = b_nums - a_nums

result = a_sub_b | b_sub_a

print(len(result))