from collections import deque

for i in range(10):
    n = int(input())
    code = deque(map(int, input().split()))

    status = True
    while status:
        for j in range(1, 5+1):
            c1 = code.popleft()
            c2 = c1 - j
            if c2 <= 0:
                c2 = 0
            code.append(c2)
            if c2 <= 0:
                status = False
                break
            
    print(f"#{i+1}", *code)
