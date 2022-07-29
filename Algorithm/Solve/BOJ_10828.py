import sys

total = int(sys.stdin.readline())
stack = []

for i in range(total):
    do = sys.stdin.readline().split()
    
    if do[0] == 'push':
        stack.append(int(do[1]))
    elif do[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif do[0] == 'size':
        print(len(stack))
    elif do[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif do[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    
