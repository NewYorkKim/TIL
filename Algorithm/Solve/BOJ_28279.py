from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    command = list(map(int, input().split()))

    if command[0] == 1:
        queue.appendleft(command[1])
    elif command[0] == 2:
        queue.append(command[1])
    elif command[0] == 3:
        if len(queue) > 0:
            tmp = queue.popleft()
            print(tmp)
        else:
            print(-1)
    elif command[0] == 4:
        if len(queue) > 0:
            tmp = queue.pop()
            print(tmp)
        else:
            print(-1)
    elif command[0] == 5:
        print(len(queue))
    elif command[0] == 6:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 7:
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    else:
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)