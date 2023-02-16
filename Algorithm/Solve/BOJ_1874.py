# n = int(input())
# targets = [int(input()) for _ in range(n)]
# result, tmp = [], []

# for i in range(1, n+1):
#     tmp.append(i)
#     result.append('+')
#     while tmp[-1] == targets[0]:
#         tmp.pop()
#         targets.remove(targets[0])
#         result.append('-')
#         if len(tmp) == 0:
#             break

# if len(targets) == 0:
#     print('\n'.join(result))
# else:
#     print('NO')

n = int(input())
stack = []
answer = []
flag = 0
cur = 1

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(num)
        answer.append('+')
        cur += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag =1
        break

if flag != 1:
    for i in answer:
        print(i)