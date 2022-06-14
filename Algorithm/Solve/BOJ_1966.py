from collections import deque
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    imp = list(map(int, sys.stdin.readline().split()))
    que = deque(imp)
    cnt = 0

    while True:
        max_num = max(que)
        if m == 0 and que[0] == max_num:
            cnt += 1
            print(cnt)
            break
        out = que.popleft()
        if out == max_num:
            cnt += 1
        else:
            que.append(out)
        if m == 0:
            m = len(que) - 1
        else:
            m -= 1
            
            

        
