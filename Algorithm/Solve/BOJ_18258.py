import sys
from collections import deque

total = int(sys.stdin.readline())
que = deque()

for i in range(total):
    do = sys.stdin.readline().split()
    
    if do[0] == 'push':
        que.append(int(do[1]))
    elif do[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif do[0] == 'size':
        print(len(que))
    elif do[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif do[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif do[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])