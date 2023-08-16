from collections import deque

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

queuestack = deque()

for idx, value in enumerate(b):
    if a[idx] == 0:
        queuestack.append(value)
        
m = int(input())  
c = list(map(int,input().split()))
answer=[]

for i in c:
    queuestack.appendleft(i)

for _ in range(m):
    answer.append(queuestack.pop()) 

print(*answer)