from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input().strip())
    que = deque(map(int, eval(input().strip())))

    reverse = 0
    flag = False
    for i in p:
        if i == "R":
            reverse += 1
        if i == "D":
            if len(que) != 0:
                if reverse % 2 == 0:
                    que.popleft()
                else:
                    que.pop()
            else:
                flag = True
                break

    if flag:
        print("error")
    else:
        que = list(map(str, que))
        if reverse % 2 == 0:
            print("[" + ",".join(que) + "]")
        else:
            que.reverse()
            print("[" + ",".join(que) + "]")
