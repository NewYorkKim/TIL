import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def do_D(n):
    res = n * 2

    if res > 9999:
        res %= 10000

    return res

def do_S(n):
    if n == 0:
        res = 9999
    else:
        res = n - 1

    return res

def do_L(n):
    pre = n % 1000
    suf = n // 1000
    res = pre * 10 + suf

    return res

def do_R(n):
    pre = n % 10
    suf = n // 10
    res = pre * 1000 + suf

    return res

def bfs(start, target):
    que = deque()
    visited = set()
    que.append((start, ""))
    visited.add(start)
    
    while que:
        num, oper = que.popleft()

        if num == target:
            print(oper)
            return 
        
        tmp = do_D(num)
        if tmp not in visited:
            visited.add(tmp)
            que.append((tmp, oper+"D"))

        tmp = do_S(num)
        if tmp not in visited:
            visited.add(tmp)
            que.append((tmp, oper+"S"))
        
        tmp = do_L(num)
        if tmp not in visited:
            visited.add(tmp)
            que.append((tmp, oper+"L"))

        tmp = do_R(num)
        if tmp not in visited:
            visited.add(tmp)
            que.append((tmp, oper+"R"))

for _ in range(t):
    a, b = map(int, input().split())
    bfs(a, b)
