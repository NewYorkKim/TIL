while True:
    line = input()
    stack = []

    if line == '.':
        break

    for i in line:
        if i == '[':
            stack.append(i)
        if i == '(':
            stack.append(i)
        if i == ']':
            if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
            else:
                stack.append(i)
                break
        if i == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
    
    if line[-1] != '.':
        print('no')
    elif len(stack) == 0:
        print('yes')
    else:
        print('no')
