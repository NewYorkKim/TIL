# n = int(input())
# numbers = list(map(int, input().split()))
# cnt = 0

# for number in numbers:
#     if number == 1:
#         continue
#     for i in range(2, number):
#             if number % i == 0:
#                 break
#     else:
#         cnt += 1

# print(cnt)

n = int(input())
numbers = list(map(int, input().split()))
cnt = len([number for number in numbers if number != 1 and all(number % i for i in range(2, number))])

print(cnt)