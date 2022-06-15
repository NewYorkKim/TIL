t = int(input())

# 문자열 인덱싱
"""
for i in range(t):
    ps = input()
    cnt = 0

    for j in range(len(ps)):
        if ps[j] == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt == -1:
                break

    if cnt == 0:
        print('YES')
    else:
        print('NO')
"""

# 스택
for i in range(t):
    ps = input()
    stack = []

    for i in ps:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')     