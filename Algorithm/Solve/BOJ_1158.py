from collections import deque

n, k = map(int, input().split())
people = deque([i+1 for i in range(n)])
result = []
tmp = 0

while True:
    if len(result) == n:
            break 
    tmp += 1
    person = str(people.popleft())
    if tmp == k:
        result.append(person)
        tmp = 0 
    else:
        people.append(person)    

print("<", ', '.join(result), ">", sep="")